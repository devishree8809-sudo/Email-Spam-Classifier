const messageBox = document.getElementById("messageBox");
const charCount = document.getElementById("charCount");

function updateCharacterCount() {
    charCount.textContent =
        messageBox.value.length + " characters";
}

messageBox.addEventListener(
    "input",
    updateCharacterCount
);

updateCharacterCount();


function clearMessage() {
    messageBox.value = "";
    updateCharacterCount();
    messageBox.focus();
}


function useSpamExample() {
    messageBox.value =
        "Congratulations! You have won a FREE prize. Click now to claim your reward!";
    updateCharacterCount();
}


function useNormalExample() {
    messageBox.value =
        "Hi, are we meeting tomorrow for the project discussion?";
    updateCharacterCount();
}


function toggleSidebar() {
    document
        .getElementById("sidebar")
        .classList.toggle("open");
}


const confidenceData =
    document.getElementById("confidenceData");

if (confidenceData) {

    const confidence =
        Number(confidenceData.dataset.confidence);

    const spamProgress =
        document.getElementById("spamProgress");

    const safeProgress =
        document.getElementById("safeProgress");

    if (spamProgress) {
        spamProgress.style.width =
            confidence + "%";
    }

    if (safeProgress) {
        safeProgress.style.width =
            confidence + "%";
    }
}