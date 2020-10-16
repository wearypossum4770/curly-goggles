import axios from 'axios'
import fs from 'fs'
import decode from 'mp4'


const customHeaders = {
	"accept": "*/*",
	"accept-language": "en-US,en;q=0.9",
	"if-range": "\"1144cc828-7f1e2e2-5a498e98c33ec\"",
	"range": "bytes=29065216-133292769",
	"sec-fetch-dest": "video",
	"sec-fetch-mode": "no-cors",
	"sec-fetch-site": "cross-site"
	}
const axiosInstance ={
	url :"https://cv-ph.rdtcdn.com/videos/202005/01/309254641/720P_1500K_309254641.mp4?4eTb9zYy_YWm5qs1AWUn_bRttWUMWwT2zUCJMHPNoOiWCNoJ5zJitP_X_QOIA5CXp0e-zZpm2HtIMy0pajFE6-Re0i6uuqQN3R0oSPKSVVrVyZWPq1e2CpQZYVmgfvUvlp1PnHFa1OEpZ8_l-oUvO-DKNkjcLVLDGUnUhcwo1Hyxw8CkLjc4koofBdOPYwJANSSyHeuRFPw",
	responseType: 'stream',
	headers:customHeaders,
	referrer: "https://www.redtube.com/33956431?",
	mode: "cors",
	referrerPolicy: "no-referrer-when-downgrade",
	body: null,
	}



const fetchNROP = async () => {
	try {
		const response = await axios(axiosInstance)
		response.data.pipe(fs.createWriteStream('video.mp4'))
	}catch (error){

console.log(error)
		}
	}


fetchNROP()
