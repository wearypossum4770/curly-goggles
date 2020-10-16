"use strict";
import axios from "axios";
import fs from "fs";
import path from "path";

const downloadFile = async () => {
  try {
    const pathObj = path.parse(process.cwd());
    //fs.createWriteStream('sample.png')
  } catch (error) {
    console.log(`\n\n\n\n${error}\n\n\n\n`);
  }
};

console.log(await downloadFile());
export default downloadFile;
