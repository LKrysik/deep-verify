/**
 * Deep Verify Unified Installer
 *
 * Main entry point for installation.
 * Supports both interactive CLI and programmatic use.
 */
const path = require('node:path');
const chalk = require('chalk');
const { runPrompts, confirmInstallation, checkExistingInstallation } = require('./prompts.js');
const { copyWorkflowFiles } = require('./generators/workflow.js');
const { generateConfig } = require('./generators/config.js');
const { writeClaudeAgent } = require('./generators/agent-claude.js');
const { writeGeminiAgent } = require('./generators/agent-gemini.js');
const { getTargetPaths } = require('./utils/paths.js');

/**
 * Run interactive installation
 * @param {string} targetDir - Target directory (defaults to cwd)
 */
async function installInteractive(targetDir = process.cwd()) {
  const projectRoot = path.resolve(targetDir);
  const { config: configPath } = getTargetPaths(projectRoot);

  console.log('\n' + '═'.repeat(59));
  console.log(chalk.cyan.bold('  Deep Verify - Module Installer'));
  console.log('═'.repeat(59));
  console.log(`\n📂 Target: ${chalk.yellow(projectRoot)}\n`);

  // Check existing installation
  const shouldProceed = await checkExistingInstallation(configPath);
  if (!shouldProceed) {
    console.log(chalk.yellow('\nInstallation cancelled.'));
    return false;
  }

  // Run prompts
  const config = await runPrompts({ targetDir: projectRoot });

  // Confirm
  const confirmed = await confirmInstallation(config, chalk);
  if (!confirmed) {
    console.log(chalk.yellow('\nInstallation cancelled.'));
    return false;
  }

  // Run installation
  return runInstallation(projectRoot, config);
}

/**
 * Run installation with provided config (non-interactive)
 * @param {string} targetDir - Target directory
 * @param {Object} config - Installation configuration
 * @param {string[]} config.patternDomains - Pattern domains to include
 * @param {string} config.stakes - Default stakes level
 * @param {string} config.reportsFolder - Reports output folder
 * @param {string[]} config.llmCli - LLM CLI tools to configure
 * @returns {Promise<boolean>} Success status
 */
async function runInstallation(targetDir, config) {
  const logger = {
    log: (msg) => console.log(msg),
    error: (msg) => console.error(msg),
  };

  try {
    // Copy workflow files
    await copyWorkflowFiles(targetDir, logger);

    // Generate config and pattern library
    await generateConfig(targetDir, config, logger);

    // Generate LLM CLI agents
    if (config.llmCli && config.llmCli.length > 0) {
      logger.log('\n🤖 Generating LLM CLI commands...');

      for (const cli of config.llmCli) {
        if (cli === 'claude') {
          await writeClaudeAgent(targetDir, config, logger);
        } else if (cli === 'gemini') {
          await writeGeminiAgent(targetDir, config, logger);
        }
      }
    }

    // Success message
    console.log(chalk.green.bold('\n✅ Installation complete!\n'));
    printStructure(config);
    printUsage(config);

    return true;
  } catch (error) {
    console.error(chalk.red(`\n❌ Installation failed: ${error.message}`));
    return false;
  }
}

/**
 * Print installed structure
 * @param {Object} config - Installation config
 */
function printStructure(config) {
  console.log('Structure created:');
  console.log(chalk.dim('  _bmad/deep-verify/'));
  console.log(chalk.dim('  ├── workflow.md'));
  console.log(chalk.dim('  ├── config.yaml'));
  console.log(chalk.dim('  ├── steps/'));
  console.log(chalk.dim('  └── data/'));
  console.log(chalk.dim('      ├── pattern-library.yaml (merged)'));
  console.log(chalk.dim('      ├── method-procedures/'));
  console.log(chalk.dim('      └── ...'));

  if (config.llmCli?.includes('claude')) {
    console.log(chalk.dim('  .claude/commands/deep-verify.md'));
  }
  if (config.llmCli?.includes('gemini')) {
    console.log(chalk.dim('  .gemini/commands/deep-verify.toml'));
  }
  if (config.reportsFolder) {
    console.log(chalk.dim(`  ${config.reportsFolder}/`));
  }
}

/**
 * Print usage instructions
 * @param {Object} config - Installation config
 */
function printUsage(config) {
  console.log('\n' + '═'.repeat(59));

  if (config.llmCli?.includes('claude')) {
    console.log(chalk.cyan('  Claude CLI: /deep-verify'));
  }
  if (config.llmCli?.includes('gemini')) {
    console.log(chalk.cyan('  Gemini CLI: @deep-verify'));
  }

  console.log(chalk.cyan('  Or: Load _bmad/deep-verify/workflow.md directly'));
  console.log(chalk.cyan('  Commands: DV (full verify) | QV (quick verify)'));
  console.log('═'.repeat(59) + '\n');
}

/**
 * Programmatic install function for BMad Core integration
 * @param {Object} options - Installation options from BMad Core
 * @param {string} options.projectRoot - Target project root
 * @param {Object} options.config - Module configuration
 * @param {Array<string>} options.installedIDEs - Installed IDE codes
 * @param {Object} options.logger - Logger instance
 * @returns {Promise<boolean>} Success status
 */
async function install(options) {
  const { projectRoot, config: moduleConfig, installedIDEs, logger } = options;

  try {
    logger.log(chalk.blue('Installing Deep Verify Module...'));

    // Map BMad config to installer config
    const config = {
      patternDomains: Array.isArray(moduleConfig.dv_pattern_domains)
        ? moduleConfig.dv_pattern_domains
        : moduleConfig.dv_pattern_domains
          ? [moduleConfig.dv_pattern_domains]
          : [],
      stakes: moduleConfig.dv_default_stakes || 'medium',
      reportsFolder: moduleConfig.dv_reports_output_folder?.replace('{project-root}/', '') || '',
      llmCli: mapIDEsToLlmCli(installedIDEs),
    };

    // Copy workflow files
    await copyWorkflowFiles(projectRoot, logger);

    // Generate config and pattern library
    await generateConfig(projectRoot, config, logger);

    // Generate LLM CLI agents based on installed IDEs
    if (config.llmCli.length > 0) {
      logger.log(chalk.cyan(`Generating commands for: ${config.llmCli.join(', ')}`));

      for (const cli of config.llmCli) {
        if (cli === 'claude') {
          await writeClaudeAgent(projectRoot, config, logger);
        } else if (cli === 'gemini') {
          await writeGeminiAgent(projectRoot, config, logger);
        }
      }
    }

    logger.log(chalk.green('Deep Verify Module installation complete'));
    return true;
  } catch (error) {
    logger.error(chalk.red(`Error installing Deep Verify module: ${error.message}`));
    return false;
  }
}

/**
 * Map IDE codes to LLM CLI names
 * @param {string[]} installedIDEs - Installed IDE codes
 * @returns {string[]} LLM CLI names
 */
function mapIDEsToLlmCli(installedIDEs) {
  if (!installedIDEs || installedIDEs.length === 0) {
    return [];
  }

  const mapping = {
    'claude-code': 'claude',
    cursor: 'claude', // Cursor uses Claude CLI format
    windsurf: 'claude',
  };

  const clis = new Set();
  for (const ide of installedIDEs) {
    if (mapping[ide]) {
      clis.add(mapping[ide]);
    }
  }

  return [...clis];
}

module.exports = {
  install,
  installInteractive,
  runInstallation,
};
