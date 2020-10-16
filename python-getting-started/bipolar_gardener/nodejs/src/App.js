import React, { useEffect, useState } from "react";
import "./App.css";
import BackEnd from "./components/BackEnd";
// import WeatherAPI from './components/WeatherAPI'
function App() {
 
  
  const [data, setData] = useState({
    loading: true,

    userHistory: "",
    userConnectionSaveData: "",
    userHasBeenActive: "",
    userIsActive: "",
    userAppVersion: "",
    userTimeStamp: "",
    userAccuracy: "",
    userLatitude: "",
    userLongitude: "",
    userSpeed: "",
    userHeading: "",
    userAltitude: "",
    userAltitudeAccuracy: "",
    serviceWorker: "",
    userAppCodeName: "",
    userAppName: "",
    userLanguage: "",
    userLanaguages: "",
    userPlatform: "",
    userProduct: "",
    userMediaSession: "",
    usersUserActivation: "",
    usersUserAgent: "",
    uservendor: "",
    userOnline: "",
    userCookieEnabled: "",
    userAcceptMimeTypes: "",
  });
  const fetchNavigation = () => {
    const {
      appCodeName,
      appVersion,
      appName,
      language,
      lanaguages,
      platform,
      product,
      mediaSession,
      userActivation,
      userAgent,
      vendor,
      onLine,
      cookieEnabled,
      vendorSub,
      productSub,
      serviceWorker,
      maxTouchPoints,
      hardwareConcurrency,
      connection: { downlink, downlinkMax, effectiveType, type, saveData, rtt },
    } = clientInformation;
    const { memory, timeOrigin, navigation, timing } = performance;
    if ("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition((position) => {
        const {
          timestamp,
          coords: {
            accuracy,
            latitude,
            longitude,
            speed,
            heading,
            altitude,
            altitudeAccuracy,
          },
        } = position;
        setData({
          userHasBeenActive: userActivation.hasBeenActive,
          userIsActive: userActivation.isActive,
          userAppVersion: appVersion,
          userTimeStamp: timestamp,
          userAccuracy: accuracy,
          userLatitude: latitude,
          userLongitude: longitude,
          userSpeed: speed,
          userHeading: heading,
          userAltitude: altitude,
          userAltitudeAccuracy: altitudeAccuracy,
          userHistory: "",

          userProductSub: productSub,
          userConnectionRTT: rtt,
          userConnectionType: type,
          userDevicePixelRatio: devicePixelRatio,
          userConnectionSaveData: saveData,
          userConnectionEffectiveType: effectiveType,
          userConnectionDownlink: downlink,
          userConnectionDownlinkMax: JSON.stringify(parseFloat(downlinkMax)),
          userCookieEnabled: cookieEnabled,
          userVendorSub: vendorSub,
          userLocalStorage: localStorage,
          userBrowserPerformance: {
            performanceTiming: {
              user_connectEnd: timing.connectEnd,
              user_connectStart: timing.connectStart,
              user_domComplete: timing.domComplete,
              user_domContentLoadedEventEnd: timing.domContentLoadedEventEnd,
              user_domContentLoadedEventStart:
                timing.domContentLoadedEventStart,
              user_domInteractive: timing.domInteractive,
              user_domLoading: timing.domLoading,
              user_domainLookupEnd: timing.domainLookupEnd,
              user_domainLookupStart: timing.domainLookupStart,
              user_fetchStart: timing.fetchStart,
              user_loadEventEnd: timing.loadEventEnd,
              user_loadEventStart: timing.loadEventStart,
              user_navigationStart: timing.navigationStart,
              user_redirectEnd: timing.redirectEnd,
              user_redirectStart: timing.redirectStart,
              user_requestStart: timing.requestStart,
              user_responseEnd: timing.responseEnd,
              user_responseStart: timing.responseStart,
              user_secureConnectionStart: timing.secureConnectionStart,
              user_unloadEventEnd: timing.unloadEventEnd,
              user_unloadEventStart: timing.unloadEventStart,
            },
            timeOrigin: timeOrigin,
            PerformanceNavigation: {
              redirectCount: navigation.redirectCount,
              type: navigation.type,
            },

            jsHeapSizeLimit: memory.jsHeapSizeLimit,
            totalJSHeapSize: memory.totalJSHeapSize,
            usedJSHeapSize: memory.usedJSHeapSize,
          },
          userHardwareConcurrency: hardwareConcurrency,
          userServiceWorker: serviceWorker.ready ? true : false,
          __comments__:
            "The Java-script value for  client-Information.connection.downlinkMax is Infinity, but it does not serialize into JSON",
          userMaxTouchPoints: maxTouchPoints,
          userAppCodeName: appCodeName,
          userAppName: appName,
          userLanguage: language,
          userLanaguages: lanaguages,
          userPlatform: platform,
          userProduct: product,
          userOnline: onLine,
          userMediaSession: {
            playbackStatus: mediaSession.playbackState,
            metadata: mediaSession.metadata,
          },

          usersUserAgent: userAgent,
          uservendor: vendor,
        });
    
      });
    }
  };

  useEffect(() => {
    fetchNavigation();
    setData({ loading: false });
  }, []);
  return <>{data.loading ? <div>LOADING...</div> : <BackEnd props={data} />}</>;
}

export default App;
