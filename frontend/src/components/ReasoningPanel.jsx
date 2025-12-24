import React from 'react';

const ReasoningPanel = ({ reasoning }) => {
    if (!reasoning) {
        return (
            <div className="panel reasoning-panel">
                <h2>CSA Reasoning</h2>
                <p style={{ color: 'var(--text-secondary)' }}>Waiting for input...</p>
            </div>
        );
    }

    const { decision, result } = reasoning;

    return (
        <div className="panel reasoning-panel">
            <h2>CSA Reasoning</h2>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
                <div style={{ background: 'rgba(59, 130, 246, 0.1)', padding: '0.75rem', borderRadius: '8px' }}>
                    <strong>Intent:</strong> {decision?.intent || 'Unknown'}
                </div>
                <div style={{ background: 'rgba(245, 158, 11, 0.1)', padding: '0.75rem', borderRadius: '8px' }}>
                    <strong>Urgency:</strong> {decision?.urgency || 'Unknown'}
                </div>
                <div style={{ background: 'rgba(16, 185, 129, 0.1)', padding: '0.75rem', borderRadius: '8px' }}>
                    <strong>Agent:</strong> {decision?.agent || 'Unknown'}
                </div>
                <div style={{ marginTop: '1rem' }}>
                    <strong>Response:</strong>
                    <p style={{ color: 'var(--text-secondary)', marginTop: '0.25rem' }}>{result?.response}</p>

                    {result?.data && (
                        <div style={{ marginTop: '0.5rem', background: 'rgba(255, 255, 255, 0.05)', padding: '0.5rem', borderRadius: '4px', fontSize: '0.9em' }}>
                            <strong>Details:</strong>
                            <ul style={{ listStyle: 'none', padding: 0, marginTop: '0.25rem' }}>
                                {Object.entries(result.data).map(([key, value]) => (
                                    <li key={key} style={{ display: 'flex', justifyContent: 'space-between' }}>
                                        <span style={{ color: 'var(--text-secondary)', textTransform: 'capitalize' }}>{key.replace('_', ' ')}:</span>
                                        <span>{value}</span>
                                    </li>
                                ))}
                            </ul>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default ReasoningPanel;
