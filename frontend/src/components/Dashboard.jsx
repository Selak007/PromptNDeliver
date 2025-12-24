import React, { useState, useEffect } from 'react';
import InputPanel from './InputPanel';
import ReasoningPanel from './ReasoningPanel';
import InsightsPanel from './InsightsPanel';
import LogsPanel from './LogsPanel';

const Dashboard = () => {
    const [reasoning, setReasoning] = useState(null);
    const [logs, setLogs] = useState([]);
    const [stats, setStats] = useState([]);
    const [error, setError] = useState(null);

    const fetchDashboardData = async () => {
        try {
            const logsRes = await fetch('http://localhost:8000/dashboard/logs');
            const statsRes = await fetch('http://localhost:8000/dashboard/stats');
            if (logsRes.ok) setLogs(await logsRes.json());
            if (statsRes.ok) setStats(await statsRes.json());
        } catch (error) {
            console.error("Failed to fetch dashboard data", error);
        }
    };

    useEffect(() => {
        fetchDashboardData();
        const interval = setInterval(fetchDashboardData, 5000); // Poll every 5s
        return () => clearInterval(interval);
    }, []);

    const handleSendMessage = async (message, customerId) => {
        setError(null);
        try {
            const response = await fetch('http://127.0.0.1:8000/csa/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message, customer_id: customerId }),
            });

            if (!response.ok) {
                throw new Error(`Server error: ${response.status}`);
            }

            const data = await response.json();
            setReasoning(data);
            fetchDashboardData();
        } catch (error) {
            console.error("Error sending message", error);
            setError(error.message);
        }
    };

    return (
        <div className="dashboard-container">
            {error && (
                <div style={{
                    gridColumn: '1 / -1',
                    background: 'rgba(239, 68, 68, 0.2)',
                    color: '#ef4444',
                    padding: '1rem',
                    borderRadius: '8px',
                    border: '1px solid #ef4444'
                }}>
                    <strong>Error:</strong> {error}
                </div>
            )}
            <InputPanel onSendMessage={handleSendMessage} />
            <ReasoningPanel reasoning={reasoning} />
            <InsightsPanel stats={stats} />
            <LogsPanel logs={logs} />
        </div>
    );
};

export default Dashboard;
