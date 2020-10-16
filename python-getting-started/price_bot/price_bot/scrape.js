const puppeteer = require('puppeteer');
const prettier = require('prettier');
const atob = require('atob');
const btoa = require('btoa');

const scriptUrlPatterns = [
  '*'
]

const requestCache = new Map();

async function interceptRequestsForPage(page) {
  const client = await page.target().createCDPSession();

  await client.send('Network.enable');

  await client.send('Network.setRequestInterception', { 
    patterns: scriptUrlPatterns.map(pattern => ({
      urlPattern: pattern, resourceType: 'Script', interceptionStage: 'HeadersReceived'
    }))
  });

  client.on('Network.requestIntercepted', async ({ interceptionId, request, responseHeaders, resourceType }) => {
    console.log(`Intercepted ${request.url} {interception id: ${interceptionId}}`);

    const response = await client.send('Network.getResponseBodyForInterception',{ interceptionId });

    const contentTypeHeader = Object.keys(responseHeaders).find(k => k.toLowerCase() === 'content-type');
    let newBody, contentType = responseHeaders[contentTypeHeader];

    if (requestCache.has(response.body)) {
      newBody = requestCache.get(response.body);
    } else {
      const bodyData = response.base64Encoded ? atob(response.body) : response.body;
      try {
        if (resourceType === 'Script') newBody = prettier.format(bodyData, { parser: 'babel' })
        else newBody === bodyData
      } catch(e) {
        console.log(`Failed to process ${request.url} {interception id: ${interceptionId}}: ${e}`);
        newBody = bodyData
      }
  
      requestCache.set(response.body, newBody);
    }

    const newHeaders = [
      'Date: ' + (new Date()).toUTCString(),
      'Connection: closed',
      'Content-Length: ' + newBody.length,
      'Content-Type: ' + contentType
    ];

    console.log(`Continuing interception ${interceptionId}`)
    client.send('Network.continueInterceptedRequest', {
      interceptionId,
      rawResponse: btoa('HTTP/1.1 200 OK' + '\r\n' + newHeaders.join('\r\n') + '\r\n\r\n' + newBody)
    });
  });
}

(async function main(){
try{
  const browser = await puppeteer.launch({
    headless:false, 
    defaultViewport:null,
    devtools: true,
    args: ['--window-size=1920,1170','--window-position=0,0']
  });

  const page = (await browser.pages())[0];

  await interceptRequestsForPage(page);

  browser.on('targetcreated', async (target) => {
    const page = await target.page();

const page = await browser.newPage();
    await page.goto(url);
    await page.waitForSelector("#emailForSignIn");
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
    await page.waitForSelector('div[class="Button__labelText-fSEjBO fXckWs"]');
    //await page.on("request", logRequest);
    await page.click('a[href="/#/books/9781119175117"]');



    await interceptRequestsForPage(page);




    
  })





  } catch (err) {
    console.log(`\n\n\n${err}\n\n\n`);
  }






})()
