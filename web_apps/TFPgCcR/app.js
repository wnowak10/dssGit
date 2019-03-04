

var url = 'https://dsproj2-api.dataiku.com//public/api/v1/nowak_3_4_19/cf/predict';

var bodyy = { "features" : {
    "userID": "1",
    "itemID": "100"
  }};

var resultt = fetch(url, {
        method: "POST", 
        mode: "no-cors", 
        cache: "no-cache", 
        credentials: "same-origin", 
        headers: {
            "Content-Type": "application/json", 
        },
        redirect: "follow", // manual, *follow, error
        referrer: "no-referrer", // no-referrer, *client
        body: JSON.stringify(bodyy), // body data type must match "Content-Type" header
    })

console.log('result', resultt);
