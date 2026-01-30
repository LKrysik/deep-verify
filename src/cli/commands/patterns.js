const fs = require('fs-extra');
const path = require('node:path');
const chalk = require('chalk');
const yaml = require('js-yaml');
const logger = require('../utils/logger.js');

/**
 * Get data directory
 */
function getDataDir() {
  return path.join(__dirname, '../../workflows/deep-verify/data');
}

/**
 * Parse multi-document YAML and extract patterns
 */
function parsePatternLibrary(content) {
  const patterns = [];
  const docs = yaml.loadAll(content);

  for (const doc of docs) {
    if (!doc) continue;

    // Check each category in the document
    const categoryKeys = [
      'definitional_contradictions',
      'theorem_violations',
      'statistical_impossibilities',
      'regulatory_contradictions',
      'ungrounded_concepts',
    ];

    for (const categoryKey of categoryKeys) {
      if (doc[categoryKey]) {
        for (const pattern of Object.values(doc[categoryKey])) {
          if (pattern && typeof pattern === 'object' && pattern.id) {
            patterns.push(pattern);
          }
        }
      }
    }
  }

  return patterns;
}

/**
 * List all impossibility patterns
 */
async function listPatterns() {
  const dataDir = getDataDir();
  const patternsPath = path.join(dataDir, 'pattern-library.yaml');

  if (!(await fs.pathExists(patternsPath))) {
    logger.error('Pattern library not found');
    return;
  }

  const content = await fs.readFile(patternsPath, 'utf8');
  const patterns = parsePatternLibrary(content);

  logger.info(`Deep Verify Pattern Library (${patterns.length} patterns)`);
  logger.log('');
  logger.log('Known impossibility patterns for rapid detection.');
  logger.log('Pattern match = +1 bonus + early exit capability.');
  logger.log('');

  // Group by category
  const categories = {
    DC: { name: 'Definitional Contradictions', patterns: [] },
    TV: { name: 'Theorem Violations', patterns: [] },
    SI: { name: 'Statistical Impossibilities', patterns: [] },
    RC: { name: 'Regulatory Contradictions', patterns: [] },
    UG: { name: 'Ungrounded Core Concepts', patterns: [] },
  };

  for (const pattern of patterns) {
    const prefix = pattern.id?.split('-')[0];
    if (categories[prefix]) {
      categories[prefix].patterns.push(pattern);
    }
  }

  for (const category of Object.values(categories)) {
    if (category.patterns.length > 0) {
      logger.log(chalk.yellow(category.name));
      for (const pattern of category.patterns) {
        const validated = pattern.validated ? chalk.green('✓') : chalk.gray('○');
        logger.log(`  ${validated} ${chalk.cyan(pattern.id)}: ${pattern.name}`);
      }
      logger.log('');
    }
  }

  logger.log(chalk.gray('Use `deep-verify patterns <id>` for details'));
}

/**
 * Show pattern details
 */
async function showPattern(patternId) {
  const dataDir = getDataDir();
  const patternsPath = path.join(dataDir, 'pattern-library.yaml');

  if (!(await fs.pathExists(patternsPath))) {
    logger.error('Pattern library not found');
    return;
  }

  const content = await fs.readFile(patternsPath, 'utf8');
  const patterns = parsePatternLibrary(content);

  const pattern = patterns.find((p) => p.id?.toLowerCase() === patternId.toLowerCase());

  if (!pattern) {
    logger.error(`Pattern ${patternId} not found`);
    logger.log('');
    logger.log('Use `deep-verify patterns` to list all patterns');
    return;
  }

  logger.info(`Pattern: ${pattern.id}`);
  logger.log('');
  logger.log(chalk.cyan('Name: ') + pattern.name);

  if (pattern.severity) {
    logger.log(chalk.cyan('Severity: ') + pattern.severity);
  }

  if (pattern.why_impossible) {
    logger.log('');
    logger.log(chalk.yellow('Why Impossible:'));
    const lines = pattern.why_impossible.trim().split('\n');
    for (const line of lines) {
      logger.log(`  ${line}`);
    }
  }

  if (pattern.detection_methods) {
    logger.log('');
    logger.log(chalk.yellow('Detection Methods:'));
    for (const method of pattern.detection_methods) {
      logger.log(`  - ${method}`);
    }
  }

  if (pattern.signals) {
    logger.log('');
    logger.log(chalk.yellow('Signals:'));
    for (const signal of pattern.signals) {
      logger.log(`  - "${signal}"`);
    }
  }

  if (pattern.check) {
    logger.log('');
    logger.log(chalk.yellow('Quick Check:'));
    logger.log(`  ${pattern.check}`);
  }

  if (pattern.theorem) {
    logger.log('');
    logger.log(chalk.gray(`Theorem: ${pattern.theorem}`));
  }

  logger.log('');
  logger.log(chalk.gray(`Validated: ${pattern.validated || 'No'}`));
}

/**
 * Patterns command
 */
async function patternsCommand(patternId) {
  await (patternId ? showPattern(patternId) : listPatterns());
}

module.exports = patternsCommand;
