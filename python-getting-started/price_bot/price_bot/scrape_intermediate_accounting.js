import puppeteer from "puppeteer";
import interceptRequestsForPage from "./interceptRequestsForPage.js";
const url = "https://ereader.chegg.com/#/books/9781119175117/recent";

const next_page =
  'button[class="navigation-button no-button horizontal-button next-button"]';
const last_page =
  'button[class="navigation-button no-button horizontal-button previous-button"]';
("https://ereader.chegg.com/#/books/9781119175117/cfi/{NEXT_PAGE}");

const Book = (async () => {
  try {
    console.log(`\n\n\nLoading Browser`);
    const browser = await puppeteer.launch({
      headless: false,
      devtools: true,
      defaultViewport: null,
      args: ["--window-size=30,30", "--window-position=0,0"],
    });
    const page = await browser.newPage();
    console.log(`\n\n\nStart navigation`);
    await page.goto(url);
    await page.waitForNavigation({ waitUntil: "domcontentloaded" });

    //a

    await page.click("#emailForSignIn");
    await page.type("#emailForSignIn", "wearypossum4770@yahoo.com", {
      delay: 10,
    });
    await page.click("#passwordForSignIn");
    await page.type("#passwordForSignIn", "C0unt3rP01s312!@", { delay: 10 });
    await page.click('button[type="submit"]');
    await page.waitForNavigation({ waitUntil: "domcontentloaded" });
    await page.waitForNavigation({ waitUntil: "networkidle0" });

    await page.reload({ waitUntil: "load" });
    console.log(`\n\n\nRELOAD COMPLETE`);
    await page.waitForNavigation({ waitUntil: "domcontentloaded" });

    await page.waitForSelector('div[class="Button__labelText-fSEjBO fXckWs"]');
    await page.waitForNavigation({ waitUntil: "domcontentloaded" });

    await page.click('a[href="/#/books/9781119175117"]');
    await page.waitForNavigation({ waitUntil: "domcontentloaded" });

    interceptRequestsForPage(page);

    //await page.on("response", grabImage);
    //await page.screenshot({path: 'example.png'});
    //await browser.close();
  } catch (err) {
    console.log(`\n\n\n${err}\n\n\n`);
  }
})();
console.log(Book);
