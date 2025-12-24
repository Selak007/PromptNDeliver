import React, { useState } from 'react';

const InputPanel = ({ onSendMessage }) => {
  const [message, setMessage] = useState('');
  const [customerId, setCustomerId] = useState('1'); // Default for demo

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!message.trim()) return;
    onSendMessage(message, parseInt(customerId));
    setMessage('');
  };

  return (
    <div className="panel input-panel">
      <h2>Live Input</h2>
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
        <div>
          <label style={{ display: 'block', marginBottom: '0.5rem', color: 'var(--text-secondary)' }}>Customer ID</label>
          <input
            type="number"
            value={customerId}
            onChange={(e) => setCustomerId(e.target.value)}
            style={{ width: '100%', boxSizing: 'border-box' }}
          />
        </div>
        <div>
          <label style={{ display: 'block', marginBottom: '0.5rem', color: 'var(--text-secondary)' }}>Message</label>
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Type your message..."
            style={{ width: '100%', boxSizing: 'border-box' }}
          />
        </div>
        <button type="submit">Send Message</button>
      </form>
    </div>
  );
};

export default InputPanel;
