const fs = require('fs-extra');
const path = require('node:path');
const chalk = require('chalk');
const logger = require('../utils/logger.js');

/**
 * Get methods data directory
 */
function getDataDir() {
  return path.join(__dirname, '../../workflows/deep-verify/data');
}

/**
 * Parse CSV line handling quoted fields
 */
function parseCSVLine(line) {
  const result = [];
  let current = '';
  let inQuotes = false;

  for (const char of line) {
    if (char === '"') {
      inQuotes = !inQuotes;
    } else if (char === ',' && !inQuotes) {
      result.push(current.trim());
      current = '';
    } else {
      current += char;
    }
  }
  result.push(current.trim());
  return result;
}

/**
 * List all verification methods
 */
async function listMethods() {
  const dataDir = getDataDir();
  const methodsPath = path.join(dataDir, 'methods.csv');

  if (!(await fs.pathExists(methodsPath))) {
    logger.error('Methods data not found');
    return;
  }

  const content = await fs.readFile(methodsPath, 'utf8');
  const lines = content.trim().split('\n');
  // Headers: num,category,method_name,description,output_pattern,when_to_load,tier
  const methods = lines.slice(1).filter((l) => l.trim());

  logger.info('Deep Verify Methods (18 total)');
  logger.log('');

  // Group by tier
  const tiers = {
    1: { name: 'Tier 1 - Mandatory (Phase 1)', methods: [] },
    2: { name: 'Tier 2 - Signal-Based (Phase 2)', methods: [] },
    3: { name: 'Tier 3 - Adversarial (Phase 3)', methods: [] },
  };

  for (const line of methods) {
    const parts = parseCSVLine(line);
    const id = parts[0]; // num
    const category = parts[1]; // category
    const name = parts[2]; // method_name
    const tier = Number.parseInt(parts[6], 10) || 2; // tier is last column

    tiers[tier]?.methods.push({ id, name, category });
  }

  for (const tier of Object.values(tiers)) {
    if (tier.methods.length > 0) {
      logger.log(chalk.yellow(tier.name));
      for (const method of tier.methods) {
        const categoryInfo = method.category ? chalk.gray(` [${method.category}]`) : '';
        logger.log(`  #${method.id} ${method.name}${categoryInfo}`);
      }
      logger.log('');
    }
  }

  logger.log(chalk.gray('Use `deep-verify methods <id>` for details'));
}

/**
 * Show method details
 */
async function showMethod(methodId) {
  const dataDir = getDataDir();
  const proceduresDir = path.join(dataDir, 'method-procedures');

  if (!(await fs.pathExists(proceduresDir))) {
    logger.error('Method procedures not found');
    return;
  }

  const files = await fs.readdir(proceduresDir);
  const methodFile = files.find((f) => f.startsWith(`${methodId}_`) || f.includes(`_${methodId}_`));

  if (!methodFile) {
    // Try with leading zeros
    const paddedId = methodId.padStart(3, '0');
    const paddedFile = files.find((f) => f.startsWith(`${paddedId}_`));

    if (!paddedFile) {
      logger.error(`Method #${methodId} not found`);
      logger.log('');
      logger.log('Use `deep-verify methods` to list all methods');
      return;
    }

    const content = await fs.readFile(path.join(proceduresDir, paddedFile), 'utf8');
    console.log(content);
    return;
  }

  const content = await fs.readFile(path.join(proceduresDir, methodFile), 'utf8');
  console.log(content);
}

/**
 * Methods command
 */
async function methodsCommand(methodId) {
  await (methodId ? showMethod(methodId) : listMethods());
}

module.exports = methodsCommand;
