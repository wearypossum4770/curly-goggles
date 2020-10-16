import https from "https";
import fs from "fs";
import path from "path";
const baseURL =
  "https://covers.vitalbook.com/vbid/9781119175117/width/320?style=preview";

const DownloadFromLink = (url) => {
  const filename = path.basename(url);
  const req = https.get(url, function (res) {
    const fileStream = fs.createWriteStream(filename);
    res.pipe(fileStream);
    //fileStream.on("error",  	err => console.log(`error writting to the steam.\n${err}`));
    //fileStream.on("close", () => callback(filename));
    //fileStream.on("finish", () => console.log(`Done!${fileStream.close()}`));
  });
  req.on("error", (err) => console.log(`Error downloading the file.\n${err}`));
};
DownloadFromLink(baseURL);
