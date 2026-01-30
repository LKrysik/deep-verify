/**
 * Configuration generator
 * Creates config.yaml and reports directory
 */
const fs = require('fs-extra');
const path = require('node:path');
const yaml = require('js-yaml');
const { getTargetPaths, getModuleRoot } = require('../utils/paths.js');
const { mergePatternLibraries } = require('../utils/yaml-merger.js');

/**
 * Generate and write config.yaml
 * @param {string} targetDir - Target project directory
 * @param {Object} config - Installation configuration
 * @param {string[]} config.patternDomains - Selected pattern domains
 * @param {string} config.stakes - Default stakes level
 * @param {string} config.reportsFolder - Reports output folder
 * @param {string[]} config.llmCli - Selected LLM CLIs
 * @param {Object} logger - Logger instance
 */
async function generateConfig(targetDir, config, logger) {
  const { config: configPath, patternLibrary: patternLibraryPath } = getTargetPaths(targetDir);

  logger.log('\n⚙️  Creating configuration...');

  // Create config.yaml
  const packageJsonPath = path.join(getModuleRoot(), 'package.json');
  const packageJson = require(packageJsonPath);
  const dvConfig = {
    version: packageJson.version,
    generated_at: new Date().toISOString(),
    pattern_domains: ['core', ...config.patternDomains],
    default_stakes: config.stakes,
    reports_folder: config.reportsFolder,
    llm_cli: config.llmCli,
    paths: {
      workflow: '_bmad/deep-verify/workflow.md',
      data: '_bmad/deep-verify/data',
      pattern_library: '_bmad/deep-verify/data/pattern-library.yaml',
    },
  };

  await fs.ensureDir(path.dirname(configPath));
  await fs.writeFile(configPath, yaml.dump(dvConfig, { lineWidth: 100 }));
  logger.log(`   ✓ Created _bmad/deep-verify/config.yaml`);

  // Create merged pattern library
  logger.log('\n📚 Creating merged pattern library...');
  const mergedContent = mergePatternLibraries(config.patternDomains);

  await fs.ensureDir(path.dirname(patternLibraryPath));
  await fs.writeFile(patternLibraryPath, mergedContent);

  const allDomains = ['core', ...config.patternDomains];
  logger.log(`   ✓ Merged ${allDomains.length} libraries into data/pattern-library.yaml`);
  logger.log(`     Included: ${allDomains.join(', ')}`);

  // Create reports directory
  if (config.reportsFolder) {
    const reportsPath = path.join(targetDir, config.reportsFolder);
    if (!(await fs.pathExists(reportsPath))) {
      await fs.ensureDir(reportsPath);
      logger.log(`   ✓ Created ${config.reportsFolder}/`);
    }
  }
}

module.exports = {
  generateConfig,
};
