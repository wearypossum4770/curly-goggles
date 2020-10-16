const { setHeadlessWhen } = require('@codeceptjs/configure');

// turn on headless mode when running with HEADLESS=true environment variable
// HEADLESS=true npx codecept run
setHeadlessWhen(process.env.HEADLESS);

exports.config = {
        tests: './tests/*_test.js',
        output: './tests/output',
        helpers: {
			MailSlurp: {
				require: '@codeceptjs/mailslurp-helper',
				apiKey: '<apiKeyFromMailSlurp>'
				},
			GraphQL: {
				endpoint: "http://localhost/graphql/",
				defaultHeaders: {
					Auth: '11111',
					'Content-Type': 'application/json',
					Accept: 'application/json',
					},
				},
			REST: {
				endpoint: "http://localhost/api/v1/",
				defaultHeaders: {
					Auth: '11111',
					'Content-Type': 'application/json',
					Accept: 'application/json',
					},
				},
            Mochawesome: {
                uniqueScreenshotNames: "true"
            },
            WebDriver: {
                url: 'https://myapp.com',
                browser: 'chrome',
                host: '127.0.0.1',
                port: 4444,
                restart: false,
                windowSize: '1920x1680',
                desiredCapabilities: {
                    chromeOptions: {
                        args: [ /*"--headless",*/ "--disable-gpu",
                            "--no-sandbox"
                        ]
                    }
                }
            },
            Puppeteer: {
                url: 'http://localhost',
                show: true,
                waitForNavigation: "networkidle0"

                windowSize: '1200x900'
            },
            MockRequest: {

            },
            Detox: {
                require: '@codeceptjs/detox-helper',
                configuration: '<detox app configuration name>',
                reloadReactNative: true,
            },
            Appium: app: "bs://<hashed app-id>",
            host: "hub-cloud.browserstack.com",
            port: 4444,
            user: "BROWSERSTACK_USER",
            key: "BROWSERSTACK_KEY",
            device: "iPhone 7"
        },
        Protractor: {
            url: "http://todomvc.com/examples/angularjs/",
            driver: "hosted",
            browser: "firefox",
            angular: false
        },

    },
    include: {
        I: './steps_file.js'
    },
    bootstrap: null,
    mocha: {
        reporterOptions: {
            reportDir: "output",
            mochaFile: "output/result.xml",
            "codeceptjs-cli-reporter": {
                stdout: "-",
                options: {
                    verbose: true,
                    steps: true,
                }
            },
            mochawesome: {
                stdout: "./output/console.log",
                options: {
                    reportDir: "./output",
                    reportFilename: "report"
                },
                "mocha-junit-reporter": {
                    stdout: "./output/console.log",
                    options: {
                        mochaFile: "./output/result.xml"
                    },
                    attachments: true //add screenshot for a failed test
                }
            }
  

        },
        name: 'npm',
        plugins: {
            wdio: {
                enabled: true,
                services: ['selenium-standalone']
            },
            retryFailedStep: {
                enabled: true
            },
            screenshotOnFail: {
                enabled: true
            }
        }
    }
    if (process.profile === "chrome-ci") {
  config.helpers.WebDriver.host =
    process.env.SELENIUM_STANDALONE_CHROME_PORT_4444_TCP_ADDR;
  // Reset config because it got overriden by BrowserStack auto detect mechanism
  config.helpers.WebDriver.protocol = "http";
  config.helpers.WebDriver.port = 4444;
}

