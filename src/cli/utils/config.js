const fs = require('fs-extra');
const path = require('node:path');

const CONFIG_FILENAME = '.deep-verify.config.json';

const DEFAULT_CONFIG = {
  reports_output_folder: '.bmad-dv/reports',
  default_stakes: null, // auto-detect
  default_mode: 'standard', // standard | blind
};

/**
 * Find project root by looking for package.json
 */
function findProjectRoot(startDir = process.cwd()) {
  let currentDir = startDir;
  while (currentDir !== path.dirname(currentDir)) {
    if (fs.existsSync(path.join(currentDir, 'package.json'))) {
      return currentDir;
    }
    currentDir = path.dirname(currentDir);
  }
  return process.cwd();
}

/**
 * Get config file path
 */
function getConfigPath(projectRoot) {
  return path.join(projectRoot, CONFIG_FILENAME);
}

/**
 * Load configuration from project
 */
async function loadConfig(projectRoot) {
  const configPath = getConfigPath(projectRoot);

  if (await fs.pathExists(configPath)) {
    try {
      const userConfig = await fs.readJson(configPath);
      return { ...DEFAULT_CONFIG, ...userConfig };
    } catch {
      return DEFAULT_CONFIG;
    }
  }

  return DEFAULT_CONFIG;
}

/**
 * Save configuration to project
 */
async function saveConfig(projectRoot, config) {
  const configPath = getConfigPath(projectRoot);
  await fs.writeJson(configPath, config, { spaces: 2 });
}

/**
 * Get a single config value
 */
async function getConfigValue(projectRoot, key) {
  const config = await loadConfig(projectRoot);
  return config[key];
}

/**
 * Set a single config value
 */
async function setConfigValue(projectRoot, key, value) {
  const config = await loadConfig(projectRoot);
  config[key] = value;
  await saveConfig(projectRoot, config);
  return config;
}

module.exports = {
  DEFAULT_CONFIG,
  CONFIG_FILENAME,
  findProjectRoot,
  getConfigPath,
  loadConfig,
  saveConfig,
  getConfigValue,
  setConfigValue,
};
