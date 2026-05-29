"use client";

import { useState } from "react";

export default function Home() {

  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");

  const sendMessage = async () => {

    const res = await fetch(
      "https://ai-support-agent-jrv-production.up.railway.app/chat",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message,
        }),
      }
    );

    const data = await res.json();

    setReply(data.reply);
  };

  return (
    <main className="p-10 max-w-2xl mx-auto">

      <h1 className="text-3xl font-bold mb-6">
        AI Support Agent
      </h1>

      <textarea
        className="border p-3 w-full"
        rows={5}
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask support question..."
      />

      <button
        onClick={sendMessage}
        className="bg-black text-white px-6 py-3 mt-4"
      >
        Send
      </button>

      {reply && (
        <div className="mt-6 border p-4">
          <h2 className="font-bold mb-2">
            AI Reply
          </h2>

          <p>{reply}</p>
        </div>
      )}

    </main>
  );
}