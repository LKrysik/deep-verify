const chalk = require('chalk');
const { findProjectRoot, loadConfig, setConfigValue, DEFAULT_CONFIG, getConfigPath } = require('../utils/config.js');
const logger = require('../utils/logger.js');

/**
 * List all config values
 */
async function listConfig() {
  const projectRoot = findProjectRoot();
  const config = await loadConfig(projectRoot);
  const configPath = getConfigPath(projectRoot);

  logger.info('Deep Verify Configuration:');
  logger.log('');

  for (const [key, value] of Object.entries(config)) {
    const defaultValue = DEFAULT_CONFIG[key];
    const isDefault = value === defaultValue;
    const displayValue = value === null ? chalk.gray('(auto)') : value;
    const defaultMark = isDefault ? chalk.gray(' (default)') : '';

    logger.log(`  ${chalk.cyan(key)}: ${displayValue}${defaultMark}`);
  }

  logger.log('');
  logger.log(chalk.gray(`Config file: ${configPath}`));
}

/**
 * Get a config value
 */
async function getConfig(key) {
  const projectRoot = findProjectRoot();
  const config = await loadConfig(projectRoot);

  if (!(key in config)) {
    logger.error(`Unknown config key: ${key}`);
    logger.log('');
    logger.log('Available keys:');
    for (const k of Object.keys(DEFAULT_CONFIG)) {
      logger.log(`  - ${k}`);
    }
    process.exit(1);
  }

  const value = config[key];
  console.log(value === null ? '' : value);
}

/**
 * Set a config value
 */
async function setConfig(key, value) {
  const projectRoot = findProjectRoot();

  if (!(key in DEFAULT_CONFIG)) {
    logger.error(`Unknown config key: ${key}`);
    logger.log('');
    logger.log('Available keys:');
    for (const k of Object.keys(DEFAULT_CONFIG)) {
      logger.log(`  - ${k}`);
    }
    process.exit(1);
  }

  // Parse value
  let parsedValue = value;
  switch (value) {
    case 'null':
    case 'auto': {
      parsedValue = null;

      break;
    }
    case 'true': {
      parsedValue = true;

      break;
    }
    case 'false': {
      parsedValue = false;

      break;
    }
    // No default
  }

  await setConfigValue(projectRoot, key, parsedValue);
  logger.success(`Set ${key} = ${parsedValue === null ? '(auto)' : parsedValue}`);
}

/**
 * Config command router
 */
async function configCommand(subcommand, key, value) {
  switch (subcommand) {
    case 'get': {
      if (!key) {
        logger.error('Please specify a config key');
        logger.log('Usage: deep-verify config get <key>');
        process.exit(1);
      }
      await getConfig(key);
      break;
    }
    case 'set': {
      if (!key || value === undefined) {
        logger.error('Please specify a key and value');
        logger.log('Usage: deep-verify config set <key> <value>');
        process.exit(1);
      }
      await setConfig(key, value);
      break;
    }
    default: {
      await listConfig();
    }
  }
}

module.exports = configCommand;
