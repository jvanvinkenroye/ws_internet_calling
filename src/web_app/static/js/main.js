/**
 * Number Transmitter JavaScript
 * Handles automatic number rotation from 1 to 9
 * Supports both local mode (manual controls) and server sync mode (API-driven)
 */

class NumberTransmitter {
    constructor() {
        // DOM elements
        this.numberDisplay = document.getElementById('current-number');
        this.startBtn = document.getElementById('start-btn');
        this.stopBtn = document.getElementById('stop-btn');
        this.resetBtn = document.getElementById('reset-btn');
        this.statusDisplay = document.getElementById('status');
        this.rotationCountDisplay = document.getElementById('rotation-count');
        this.syncToggle = document.getElementById('sync-toggle');

        // State variables
        this.currentNumber = 1;
        this.intervalId = null;
        this.isRunning = false;
        this.rotationCount = 0;
        this.serverSyncMode = false;

        // Bind event listeners
        this.initEventListeners();
    }

    /**
     * Initialize event listeners for control buttons
     */
    initEventListeners() {
        this.startBtn.addEventListener('click', () => this.start());
        this.stopBtn.addEventListener('click', () => this.stop());
        this.resetBtn.addEventListener('click', () => this.reset());

        // Add sync toggle listener if element exists
        if (this.syncToggle) {
            this.syncToggle.addEventListener('change', (e) => this.toggleSyncMode(e.target.checked));
        }
    }

    /**
     * Start the number rotation
     */
    start() {
        if (this.isRunning) {
            return;
        }

        this.isRunning = true;
        this.updateStatus('Running');
        this.startBtn.disabled = true;
        this.stopBtn.disabled = false;

        // Start interval to rotate numbers every second
        this.intervalId = setInterval(() => {
            this.rotateNumber();
        }, 1000);

        console.log('Number transmitter started');
    }

    /**
     * Stop the number rotation
     */
    stop() {
        if (!this.isRunning) {
            return;
        }

        this.isRunning = false;
        this.updateStatus('Stopped');
        this.startBtn.disabled = false;
        this.stopBtn.disabled = true;

        // Clear the interval
        if (this.intervalId) {
            clearInterval(this.intervalId);
            this.intervalId = null;
        }

        console.log('Number transmitter stopped');
    }

    /**
     * Reset the transmitter to initial state
     */
    reset() {
        this.stop();
        this.currentNumber = 1;
        this.rotationCount = 0;
        this.updateDisplay();
        this.updateRotationCount();
        console.log('Number transmitter reset');
    }

    /**
     * Rotate to the next number (1-9 cycle)
     */
    rotateNumber() {
        this.currentNumber++;

        // Wrap around to 1 after reaching 9
        if (this.currentNumber > 9) {
            this.currentNumber = 1;
            this.rotationCount++;
            this.updateRotationCount();
        }

        this.updateDisplay();
        console.log(`Current number: ${this.currentNumber}`);
    }

    /**
     * Update the number display with animation
     */
    updateDisplay() {
        // Add animation effect
        this.numberDisplay.style.transform = 'scale(1.2)';
        this.numberDisplay.textContent = this.currentNumber;

        // Reset animation after 200ms
        setTimeout(() => {
            this.numberDisplay.style.transform = 'scale(1)';
        }, 200);
    }

    /**
     * Update the status display
     *
     * @param {string} status - The status text to display
     */
    updateStatus(status) {
        this.statusDisplay.textContent = status;

        // Update status color
        if (status === 'Running') {
            this.statusDisplay.style.color = '#48bb78';
        } else {
            this.statusDisplay.style.color = '#f56565';
        }
    }

    /**
     * Update the rotation count display
     */
    updateRotationCount() {
        this.rotationCountDisplay.textContent = this.rotationCount;
    }

    /**
     * Toggle between local mode and server sync mode
     *
     * @param {boolean} enableSync - Whether to enable server sync
     */
    toggleSyncMode(enableSync) {
        this.serverSyncMode = enableSync;

        if (enableSync) {
            // Stop local rotation
            this.stop();

            // Disable manual controls
            this.startBtn.disabled = true;
            this.stopBtn.disabled = true;
            this.resetBtn.disabled = true;

            // Start server sync
            this.updateStatus('Syncing with Server');
            this.startServerSync();
            console.log('Server sync mode enabled');
        } else {
            // Stop server sync
            this.stopServerSync();

            // Re-enable manual controls
            this.startBtn.disabled = false;
            this.stopBtn.disabled = true;
            this.resetBtn.disabled = false;

            this.updateStatus('Stopped');
            console.log('Server sync mode disabled');
        }
    }

    /**
     * Start synchronizing with the server API
     */
    startServerSync() {
        // Fetch immediately
        this.fetchFromServer();

        // Set up interval to fetch from server every 500ms
        this.intervalId = setInterval(() => {
            this.fetchFromServer();
        }, 500);
    }

    /**
     * Stop server synchronization
     */
    stopServerSync() {
        if (this.intervalId) {
            clearInterval(this.intervalId);
            this.intervalId = null;
        }
    }

    /**
     * Fetch current number from the server API
     */
    async fetchFromServer() {
        try {
            const response = await fetch('/api/number');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            const serverNumber = data.number;
            const totalCycles = data.total_cycles;

            // Update display if number changed
            if (this.currentNumber !== serverNumber) {
                this.currentNumber = serverNumber;
                this.rotationCount = totalCycles;
                this.updateDisplay();
                this.updateRotationCount();
                console.log(`Server number: ${this.currentNumber}, Cycles: ${totalCycles}`);
            }
        } catch (error) {
            console.error('Error fetching from server:', error);
            this.updateStatus('Server Error');
        }
    }
}

// Initialize the number transmitter when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    const transmitter = new NumberTransmitter();
    console.log('Number Transmitter initialized');
});
