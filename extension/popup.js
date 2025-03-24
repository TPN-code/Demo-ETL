document.getElementById("runScript").addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.scripting.executeScript({
            target: { tabId: tabs[0].id },
            function: runInConsole
        });
    });
});

// Function to be executed in the Console
function runInConsole() {
    console.log("%cHello from the Chrome Extension!", "color: blue; font-size: 16px; font-weight: bold;");
    alert("Console script executed! Check DevTools Console (F12).");
}
