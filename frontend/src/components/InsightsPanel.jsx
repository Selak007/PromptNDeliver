import React, { useEffect, useState } from 'react';

const InsightsPanel = ({ stats }) => {
    return (
        <div className="panel insights-panel">
            <h2>Insights</h2>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
                <div style={{ background: 'rgba(255, 255, 255, 0.05)', padding: '1rem', borderRadius: '8px' }}>
                    <h3 style={{ marginTop: 0, fontSize: '1rem', color: 'var(--text-secondary)' }}>Top Issues</h3>
                    {stats && stats.length > 0 ? (
                        <ul style={{ paddingLeft: '1.2rem', margin: 0 }}>
                            {stats.map((stat) => (
                                <li key={stat.memory_id}>{stat.issue_type} ({stat.frequency})</li>
                            ))}
                        </ul>
                    ) : (
                        <p style={{ fontSize: '0.9rem' }}>No data yet</p>
                    )}
                </div>
                <div style={{ background: 'rgba(255, 255, 255, 0.05)', padding: '1rem', borderRadius: '8px' }}>
                    <h3 style={{ marginTop: 0, fontSize: '1rem', color: 'var(--text-secondary)' }}>System Status</h3>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--success)' }}>
                        <span style={{ width: '8px', height: '8px', borderRadius: '50%', background: 'var(--success)' }}></span>
                        Operational
                    </div>
                </div>
            </div>
        </div>
    );
};

export default InsightsPanel;
