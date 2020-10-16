import puppeteer from "puppeteer";
import fs from "fs";
import path from "path";

const interceptRequestsForPage = async (page) => {
  const client = await page.target().createCDPSession();

  await client.send("Network.enable");

  await client.send("Network.setRequestInterception", {
    patterns: scriptUrlPatterns.map((pattern) => ({
      urlPattern: pattern,
      resourceType: "Script",
      interceptionStage: "HeadersReceived",
    })),
  });

  client.on(
    "Network.requestIntercepted",
    async ({ interceptionId, request, responseHeaders, resourceType }) => {
      console.log(
        `Intercepted ${request.url} {interception id: ${interceptionId}}`
      );

      const response = await client.send(
        "Network.getResponseBodyForInterception",
        { interceptionId }
      );

      const contentTypeHeader = Object.keys(responseHeaders).find(
        (k) => k.toLowerCase() === "content-type"
      );
      let newBody,
        contentType = responseHeaders[contentTypeHeader];

      if (requestCache.has(response.body)) {
        newBody = requestCache.get(response.body);
      } else {
        const bodyData = response.base64Encoded
          ? atob(response.body)
          : response.body;
        try {
          if (resourceType === "Script")
            newBody = prettier.format(bodyData, { parser: "babel" });
          else newBody === bodyData;
        } catch (e) {
          console.log(
            `Failed to process ${request.url} {interception id: ${interceptionId}}: ${e}`
          );
          newBody = bodyData;
        }

        requestCache.set(response.body, newBody);
      }

      const newHeaders = [
        "Date: " + new Date().toUTCString(),
        "Connection: closed",
        "Content-Length: " + newBody.length,
        "Content-Type: " + contentType,
      ];

      console.log(`Continuing interception ${interceptionId}`);
      client.send("Network.continueInterceptedRequest", {
        interceptionId,
        rawResponse: btoa(
          "HTTP/1.1 200 OK" +
            "\r\n" +
            newHeaders.join("\r\n") +
            "\r\n\r\n" +
            newBody
        ),
      });
    }
  );
};
export default interceptRequestsForPage;
