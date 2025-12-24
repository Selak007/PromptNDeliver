import React from 'react';

const LogsPanel = ({ logs }) => {
    return (
        <div className="panel logs-panel" style={{ gridColumn: '1 / -1' }}>
            <h2>System Logs</h2>
            <div style={{ maxHeight: '200px', overflowY: 'auto' }}>
                {logs && logs.length > 0 ? (
                    logs.map((log) => (
                        <div key={log.log_id} className="log-item">
                            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.25rem' }}>
                                <strong style={{ color: 'var(--accent-color)' }}>{log.agent_name}</strong>
                                <span className="timestamp">{new Date(log.timestamp).toLocaleTimeString()}</span>
                            </div>
                            <div style={{ color: 'var(--text-secondary)' }}>{log.action_taken}</div>
                        </div>
                    ))
                ) : (
                    <p style={{ color: 'var(--text-secondary)' }}>No logs available</p>
                )}
            </div>
        </div>
    );
};

export default LogsPanel;
