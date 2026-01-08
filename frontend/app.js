let conversation = [];
const MAX_HISTORY = 8;
const API_KEY = "english-assistant-secret-123";

let currentMode = null;

const chat = document.getElementById("chat");
const input = document.getElementById("inputText");
const sendBtn = document.getElementById("sendBtn");
const inputArea = document.getElementById("inputArea");
const modeSelect = document.getElementById("modeSelect");
const toggle = document.getElementById("themeToggle");

function addMessage(text, type) {
    const div = document.createElement("div");
    div.className = `message ${type}`;
    div.textContent = text;
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
}

function setMode(mode) {
    currentMode = mode;
    modeSelect.classList.add("hidden");
    inputArea.classList.remove("hidden");

    if (mode === "grammar") {
        addMessage(
            "Grammar Correction Mode enabled. Enter a sentence to correct.",
            "bot"
        );
    } else {
        addMessage(
            "Chat Mode enabled. Ask anything or clarify your doubts.",
            "bot"
        );
    }
}

async function sendMessage() {
    const text = input.value.trim();
    if (!text || !currentMode) return;

    // Show user message
    addMessage(text, "user");
    input.value = "";
    sendBtn.disabled = true;

    // 🔥 ADD USER MESSAGE TO MEMORY
    conversation.push({
        role: "user",
        content: text
    });

    // Limit memory size
    if (conversation.length > MAX_HISTORY * 2) {
        conversation = conversation.slice(-MAX_HISTORY * 2);
    }

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-API-KEY": API_KEY
            },
            body: JSON.stringify({
                mode: currentMode,
                messages: conversation
            })
        });

        const data = await response.json();
        if (!response.ok) throw new Error();

        // 🔥 SAVE AI RESPONSE TO MEMORY
        conversation.push({
            role: "assistant",
            content: data.reply
        });

        addMessage(data.reply, "bot");

    } catch (err) {
        addMessage("❌ Error processing request.", "bot");
    } finally {
        sendBtn.disabled = false;
    }
}


sendBtn.addEventListener("click", sendMessage);

input.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

// Dark mode
toggle.addEventListener("click", () => {
    document.body.classList.toggle("dark");
    toggle.textContent =
        document.body.classList.contains("dark") ? "☀️" : "🌙";
});
