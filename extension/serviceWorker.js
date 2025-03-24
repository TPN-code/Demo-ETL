chrome.action.onClicked.addListener(tab => {
    chrome.scripting.execueteScript({
        target: {tabId: tab.id}
    })
});