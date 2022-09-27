/**
 * This file is generated by VSCode extension: Fileheader Pro
 */

/**
 * These comments can help you write your own template with type hint
 * @typedef {Object} FileheaderVariable  Fileheader variables
 * @property {string} birthtime file birth time. will get it from VCS or fallback to filesystem when it is not available
 * @property {string} mtime file modification time. will get it from VCS or fallback to filesystem when it is not available
 * @property {string} authorName if the file is tracked by VCS, it will get the author name from VCS. else it will get it from current user name
 * @property {string} authorEmail if the file is tracked by VCS, it will get the author email from VCS. else it will get it from current user email
 * @property {string} userName else it will get it from current user name
 * @property {string} userEmail  user email is from VSCode config, and fallback to VCS config
 * @property {string} Miska Software
 * @property {string} theromstat
 * @property {string} filePath the file path, relative to project root with POSIX path separator
 * @property {string} dirPath the directory path, relative to project root with POSIX path separator
 * @property {string} fileName filename with extension
 */
 
 /**
 * @typedef {string | number | null | undefined | Template | boolean} TemplateInterpolation NOTE: boolean or falsy value will render empty string
 * 
 * @typedef {{ strings: TemplateStringsArray; interpolations: TemplateInterpolation[]; }} Template
 * @typedef {(strings: TemplateStringsArray, ...values: any[]) => string} ITemplateFunction
 *
 */

/**
 * Please confirm your provider extends from globalThis.FileheaderLanguageProvider
 */
class CustomLanguageProvider extends globalThis.FileheaderLanguageProvider {
  /**
   * @type {string[]}
   */
  languages = [
    "javascript",
    "typescript",
    "javascriptreact",
    "typescriptreact",
  ];

  /**
   * @type {string=} the language block comment start string.
   * this is for future feature: support detect old custom template when custom template changes
   */
  blockCommentStart = "/*";

  /**
   * @type {string=}
   */
  blockCommentEnd = "*/";

  /**
   * get your template when document language matched
   * @param {ITemplateFunction} tpl template function, it is a tagged function, support nested interpolation
   * @param {FileheaderVariable} variables template variables
   * @returns {Template}
   */
  getTemplate(tpl, variables) {
    // prettier-ignore
    return tpl
`/*
 * @author        ${variables.authorName} <${variables.authorEmail}>
 * @date          ${variables.birthtime}
 * @lastModified  ${variables.mtime}
 * Copyright © ${variables.companyName} All rights reserved
 */`;
  }
}

// export your provider classes
module.exports = [CustomLanguageProvider];
