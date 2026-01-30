/**
 * Workflow file generator
 * Copies workflow files from src/core to target directory
 */
const fs = require('fs-extra');
const path = require('node:path');
const { getCoreDir, getTargetPaths } = require('../utils/paths.js');

/**
 * Copy workflow files to target project
 * @param {string} targetDir - Target project directory
 * @param {Object} logger - Logger instance
 * @returns {Promise<number>} Number of files copied
 */
async function copyWorkflowFiles(targetDir, logger) {
  const srcDir = getCoreDir();
  const { bmadRoot } = getTargetPaths(targetDir);

  logger.log('\n📁 Copying workflow files...');

  await fs.ensureDir(bmadRoot);

  // Copy workflow.md
  await fs.copy(path.join(srcDir, 'workflow.md'), path.join(bmadRoot, 'workflow.md'), {
    overwrite: true,
  });

  // Copy steps/
  await fs.copy(path.join(srcDir, 'steps'), path.join(bmadRoot, 'steps'), { overwrite: true });

  // Copy data/ (except pattern-library.yaml which is generated)
  const dataDir = path.join(srcDir, 'data');
  const destDataDir = path.join(bmadRoot, 'data');
  await fs.ensureDir(destDataDir);

  // Copy all data files and subdirectories
  const dataItems = await fs.readdir(dataDir, { withFileTypes: true });

  for (const item of dataItems) {
    // Skip pattern-library.yaml (it's generated during install)
    if (item.name === 'pattern-library.yaml') continue;

    const srcPath = path.join(dataDir, item.name);
    const destPath = path.join(destDataDir, item.name);

    await fs.copy(srcPath, destPath, { overwrite: true });
  }

  // Count total files
  const fileCount = countFiles(bmadRoot);
  logger.log(`   ✓ Copied ${fileCount} files to _bmad/deep-verify/`);

  return fileCount;
}

/**
 * Count files in a directory recursively
 * @param {string} dir - Directory path
 * @returns {number} File count
 */
function countFiles(dir) {
  let count = 0;
  const items = fs.readdirSync(dir, { withFileTypes: true });

  for (const item of items) {
    if (item.isDirectory()) {
      count += countFiles(path.join(dir, item.name));
    } else {
      count++;
    }
  }

  return count;
}

module.exports = {
  copyWorkflowFiles,
};
