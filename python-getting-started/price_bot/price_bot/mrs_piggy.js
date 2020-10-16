import puppeteer from "puppeteer";
const url = "https://docs.scrapy.org/en/latest/topics/media-pipeline.html"

const interceptRequestsForPage = async (page) => {
	console.log("i'm in interceptRequestsForPage function'")



	}
(async function main() {
    try {
      const browser = await puppeteer.launch({
        headless: false,
        defaultViewport: null,
        devtools: true,
        args: ["--window-size=1920,1170", "--window-position=0,0"],
      });

  

        const page = await browser.newPage();
        await page.goto(url);

         await interceptRequestsForPage(page);
 
    } catch (err) {
      console.log(`\n\n\n${err}\n\n\n`);
    }
  }
)();
