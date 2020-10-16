import axios from "axios";
import fs from "fs";
const axiosObject = {
  url:
    "https://cv-ph.rdtcdn.com/videos/202005/01/309254641/720P_1500K_309254641.mp4?4eTb9zYy_YWm5qs1AWUn_bRttWUMWwT2zUCJMHPNoOiWCNoJ5zJitP_X_QOIA5CXp0e-zZpm2HtIMy0pajFE6-Re0i6uuqQN3R0oSPKSVVrVyZWPq1e2CpQZYVmgfvUvlp1PnHFa1OEpZ8_l-oUvO-DKNkjcLVLDGUnUhcwo1Hyxw8CkLjc4koofBdOPYwJANSSyHeuRFPw",
  responseType: "stream",
  onDownloadProgress: function (progressEvent) {
    // Do whatever you want with the native progress event

    console.log(progressEvent.loaded / progressEvent.total);
  },
  headers: {
    accept: "*/*",
    "accept-language": "en-US,en;q=0.9",
    "if-range": '"1144cc828-7f1e2e2-5a498e98c33ec"',
    range: "bytes=29065216-133292769",
    "sec-fetch-dest": "video",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
  },
  referrer: "https://www.redtube.com/33956431?",
  referrerPolicy: "no-referrer-when-downgrade",
  body: null,
  method: "GET",
  mode: "cors",
};

const url =
  "https://cv-ph.rdtcdn.com/videos/202005/01/309254641/720P_1500K_309254641.mp4?4eTb9zYy_YWm5qs1AWUn_bRttWUMWwT2zUCJMHPNoOiWCNoJ5zJitP_X_QOIA5CXp0e-zZpm2HtIMy0pajFE6-Re0i6uuqQN3R0oSPKSVVrVyZWPq1e2CpQZYVmgfvUvlp1PnHFa1OEpZ8_l-oUvO-DKNkjcLVLDGUnUhcwo1Hyxw8CkLjc4koofBdOPYwJANSSyHeuRFPw";

const fetchNROP = () => {
  axios(url, axiosObject).then((response) =>
    response.data.pipe(fs.createWriteStream("ada_lovelace.mp4"))
  );
};

console.log(fetchNROP());
