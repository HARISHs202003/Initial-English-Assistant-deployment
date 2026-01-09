let currentMode = null;
let conversation = [];

const chat = document.getElementById("chat");
const input = document.getElementById("inputText");
const sendBtn = document.getElementById("sendBtn");
const inputArea = document.getElementById("inputArea");
const modeSelect = document.getElementById("modeSelect");
const toggle = document.getElementById("themeToggle");
const backBtn = document.getElementById("backBtn");
const title = document.getElementById("title");

function addMessage(text, type) {
    const div = document.createElement("div");
    div.className = `message ${type}`;
    div.textContent = text;
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
}

function setMode(mode) {
    currentMode = mode;
    conversation = [];
    chat.innerHTML = "";

    modeSelect.classList.add("hidden");
    inputArea.classList.remove("hidden");
    backBtn.classList.remove("hidden");

    const modeTitles = {
        grammar: "Grammar Correction",
        chat: "Chat Mode",
        business: "Business Idea Bot",
        trb_geo: "TRB Geography Tutor"
    };
    
    const modeMessages = {
        grammar: "✍️ Grammar mode enabled. Enter a sentence.",
        chat: "💬 Chat mode enabled. Ask anything.",
        business: "💼 Business Idea Bot activated. Ask about India & Tamil Nadu business ideas.",
        trb_geo: "📘 TRB Geography Tutor activated. Let’s prepare smartly!"
    };
    
    title.textContent = modeTitles[mode];
    addMessage(modeMessages[mode], "bot");
    
}

function goBack() {
    currentMode = null;
    conversation = [];
    chat.innerHTML = "";

    inputArea.classList.add("hidden");
    modeSelect.classList.remove("hidden");
    backBtn.classList.add("hidden");

    title.textContent = "English Assistant";
}

async function sendMessage() {
    const text = input.value.trim();
    if (!text || !currentMode) return;

    addMessage(text, "user");
    input.value = "";
    sendBtn.disabled = true;

    conversation.push({ role: "user", content: text });

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                mode: currentMode,
                messages: conversation
            })
        });

        const data = await response.json();
        if (!response.ok) throw new Error();

        conversation.push({ role: "assistant", content: data.reply });
        addMessage(data.reply, "bot");

    } catch {
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

toggle.addEventListener("click", () => {
    document.body.classList.toggle("dark");
    toggle.textContent =
        document.body.classList.contains("dark") ? "☀️" : "🌙";
});

backBtn.addEventListener("click", goBack);
