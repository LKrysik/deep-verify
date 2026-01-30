const path = require('node:path');

/**
 * Get module root directory (where package.json lives)
 * @returns {string}
 */
function getModuleRoot() {
  return path.join(__dirname, '..', '..', '..');
}

/**
 * Get core data directory path
 * @returns {string}
 */
function getCoreDir() {
  return path.join(getModuleRoot(), 'src', 'core');
}

/**
 * Get pattern libraries source directory
 * @returns {string}
 */
function getPatternLibrariesDir() {
  return path.join(getCoreDir(), 'data', 'pattern-libraries');
}

/**
 * Build target paths for installation
 * @param {string} targetDir - Target project directory
 * @returns {Object} Target paths
 */
function getTargetPaths(targetDir) {
  return {
    bmadRoot: path.join(targetDir, '_bmad', 'deep-verify'),
    workflow: path.join(targetDir, '_bmad', 'deep-verify', 'workflow.md'),
    steps: path.join(targetDir, '_bmad', 'deep-verify', 'steps'),
    data: path.join(targetDir, '_bmad', 'deep-verify', 'data'),
    config: path.join(targetDir, '_bmad', 'deep-verify', 'config.yaml'),
    patternLibrary: path.join(targetDir, '_bmad', 'deep-verify', 'data', 'pattern-library.yaml'),
    claudeCommand: path.join(targetDir, '.claude', 'commands', 'deep-verify.md'),
    geminiCommand: path.join(targetDir, '.gemini', 'commands', 'deep-verify.toml'),
  };
}

module.exports = {
  getModuleRoot,
  getCoreDir,
  getPatternLibrariesDir,
  getTargetPaths,
};
