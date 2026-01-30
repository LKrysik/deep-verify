const { loadPatternDomains } = require('./utils/yaml-merger.js');

/**
 * Get all installation prompts
 * @returns {Promise<Object>} User answers
 */
async function runPrompts() {
  const { input, checkbox, select } = await import('@inquirer/prompts');

  // Load available pattern domains
  const patternDomains = loadPatternDomains();

  // Reports folder
  const reportsFolder = await input({
    message: 'Where should verification reports be saved?',
    default: '_bmad-output/deep-verify-reports',
  });

  // LLM CLI selection
  const llmCli = await checkbox({
    message: 'Which LLM CLI tools to configure?',
    choices: [
      { name: 'Claude CLI (.claude/commands/)', value: 'claude', checked: true },
      { name: 'Gemini CLI (.gemini/commands/)', value: 'gemini', checked: false },
    ],
  });

  // Pattern domains selection
  const allOption = {
    name: '★ ALL - Select all domain libraries',
    value: '__ALL__',
  };
  const domainChoices = [
    allOption,
    ...patternDomains.map((d) => ({
      name: d.name,
      value: d.value,
      checked: d.checked,
    })),
  ];

  const selectedPatternDomains = await checkbox({
    message: 'Which pattern libraries to include?\n  (Core is always included)',
    choices: domainChoices,
    pageSize: 12,
  });

  // Handle "All" selection
  let domains = selectedPatternDomains;
  if (domains.includes('__ALL__')) {
    domains = patternDomains.map((d) => d.value);
  }

  // Stakes level
  const stakes = await select({
    message: 'Default stakes level?',
    choices: [
      { name: 'LOW - Minor rework, reversible decisions', value: 'low' },
      { name: 'MEDIUM - Significant rework possible', value: 'medium' },
      { name: 'HIGH - Major damage, safety, reputation risk', value: 'high' },
    ],
    default: 'medium',
  });

  return {
    reportsFolder,
    llmCli,
    patternDomains: domains,
    stakes,
  };
}

/**
 * Ask for confirmation before proceeding
 * @param {Object} config - Configuration to confirm
 * @param {Object} chalk - Chalk instance for colors
 * @returns {Promise<boolean>}
 */
async function confirmInstallation(config, chalk) {
  const { confirm } = await import('@inquirer/prompts');

  console.log('\n' + '─'.repeat(59));
  console.log(chalk.cyan('Configuration:'));
  console.log(`  Reports folder: ${chalk.white(config.reportsFolder)}`);
  console.log(`  LLM CLI: ${chalk.white(config.llmCli.length > 0 ? config.llmCli.join(', ') : 'none')}`);
  console.log(
    `  Pattern domains: ${chalk.white('core' + (config.patternDomains.length > 0 ? ' + ' + config.patternDomains.join(', ') : ''))}`,
  );
  console.log(`  Default stakes: ${chalk.white(config.stakes.toUpperCase())}`);
  console.log('─'.repeat(59));

  return confirm({
    message: 'Proceed with installation?',
    default: true,
  });
}

/**
 * Check if Deep Verify is already installed and ask about reinstall
 * @param {string} configPath - Path to existing config
 * @returns {Promise<boolean>} Whether to proceed
 */
async function checkExistingInstallation(configPath) {
  const fs = require('fs-extra');
  const { confirm } = await import('@inquirer/prompts');

  if (await fs.pathExists(configPath)) {
    return confirm({
      message: 'Deep Verify is already installed. Reinstall?',
      default: false,
    });
  }
  return true;
}

module.exports = {
  runPrompts,
  confirmInstallation,
  checkExistingInstallation,
};
