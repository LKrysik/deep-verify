const chalk = require('chalk');

/**
 * CLI Logger - compatible with installer.js API
 */
const logger = {
  log: (message) => console.log(message),
  info: (message) => console.log(chalk.blue(message)),
  success: (message) => console.log(chalk.green(message)),
  warn: (message) => console.log(chalk.yellow(message)),
  error: (message) => console.error(chalk.red(message)),
  debug: (message) => {
    if (process.env.DEBUG) {
      console.log(chalk.gray(`[debug] ${message}`));
    }
  },
};

module.exports = logger;
