# Project Overview

## Introduction

The "Nummernsender im Internet" (Number Transmitter on the Internet) project is a comprehensive seminar that teaches modern web development, API design, and IoT programming using Python and Raspberry Pi Pico W.

## What You'll Build

### Three Main Components

#### 1. Web Application
An interactive web page that displays numbers 1-9 in a continuous rotation, changing every second.

**Key Features:**
- Modern, responsive design
- Real-time number display
- Interactive controls (Start, Stop, Reset)
- Cycle counter
- Mobile-friendly interface

**Technology Stack:**
- Backend: Python Flask
- Frontend: HTML5, CSS3, Vanilla JavaScript
- Design: Gradient backgrounds, smooth animations

#### 2. REST API
A machine-readable API that provides access to the number transmission system.

**Endpoints:**
- Current number with metadata
- Sequence configuration
- System status and uptime

**Technology Stack:**
- Python Flask
- Flask-CORS for cross-origin requests
- JSON response format
- RESTful design principles

#### 3. IoT Applications
Six MicroPython programs for Raspberry Pi Pico W demonstrating progressive complexity:

1. **Basic LED Blink** - Introduction to GPIO control
2. **WiFi Connection** - Network connectivity basics
3. **Signal Monitor** - Measuring and displaying WiFi strength
4. **Signal to Blink** - Converting data to visual feedback
5. **API Consumer** - Fetching and processing remote data
6. **Access Point** - Creating a wireless network with web interface

## Learning Objectives

By completing this project, you will:

### Python Development
- ✅ Build Flask web applications
- ✅ Design RESTful APIs
- ✅ Handle HTTP requests and responses
- ✅ Implement CORS for cross-origin access
- ✅ Structure Python projects with best practices

### Frontend Development
- ✅ Create responsive HTML layouts
- ✅ Style with modern CSS (gradients, animations)
- ✅ Implement interactive JavaScript
- ✅ Handle DOM manipulation
- ✅ Work with browser APIs

### IoT & Embedded Systems
- ✅ Program Raspberry Pi Pico W with MicroPython
- ✅ Control GPIO pins and LEDs
- ✅ Establish WiFi connections
- ✅ Measure signal strength
- ✅ Consume REST APIs from microcontrollers
- ✅ Create WiFi access points
- ✅ Serve web pages from embedded devices

### Networking
- ✅ Understand client-server architecture
- ✅ Work with HTTP protocol
- ✅ Debug network connectivity
- ✅ Configure WiFi networks
- ✅ Handle DHCP and IP addressing

### Documentation
- ✅ Write comprehensive guides
- ✅ Create troubleshooting documentation
- ✅ Use MkDocs for project documentation
- ✅ Organize knowledge effectively

## Project Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    User Devices                         │
│  (Web Browser, Mobile, Raspberry Pi Pico W)            │
└────────────┬──────────────────────────┬─────────────────┘
             │                          │
             │ HTTP                     │ HTTP
             ▼                          ▼
┌─────────────────────┐      ┌──────────────────────┐
│   Web Application   │      │    REST API          │
│   (Flask)           │      │    (Flask)           │
│   Port: 5000        │      │    Port: 5001        │
│                     │      │                      │
│   - HTML/CSS/JS     │      │   - JSON Responses   │
│   - Interactive UI  │      │   - CORS Enabled     │
│   - Number Display  │      │   - Status Endpoints │
└─────────────────────┘      └──────────────────────┘
                                       ▲
                                       │ WiFi
                                       │
                         ┌─────────────┴──────────────┐
                         │  Raspberry Pi Pico W      │
                         │  (MicroPython)            │
                         │                           │
                         │  - WiFi Client            │
                         │  - API Consumer           │
                         │  - LED Display            │
                         │  - Access Point Mode      │
                         └───────────────────────────┘
```

## Technology Stack

### Backend
- **Python 3.12+**: Modern Python with type hints
- **Flask 3.x**: Lightweight web framework
- **Flask-CORS**: Cross-origin resource sharing
- **uv**: Fast Python package manager

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with gradients and animations
- **JavaScript ES6+**: Modern JavaScript features
- **No frameworks**: Vanilla JS for learning fundamentals

### Embedded Systems
- **MicroPython**: Python for microcontrollers
- **Raspberry Pi Pico W**: RP2040-based microcontroller with WiFi
- **Thonny IDE**: Beginner-friendly Python IDE

### Documentation
- **MkDocs**: Static site generator for project documentation
- **Material Theme**: Modern, responsive documentation theme
- **Markdown**: Easy-to-write documentation format

## Use Cases

### Educational
- Learning web development fundamentals
- Understanding API design principles
- Introduction to IoT programming
- Practicing documentation skills

### Demonstrations
- Teaching number transmission concepts
- Showing client-server communication
- Demonstrating wireless data transfer
- Explaining REST API concepts

### Prototyping
- Template for Flask applications
- API design patterns
- MicroPython project structure
- Documentation framework

## Project Timeline

Recommended learning path:

### Week 1: Setup & Web Development
- Install tools (Python, Thonny)
- Build web application
- Create REST API
- Test locally

### Week 2: IoT Basics
- Flash Raspberry Pi Pico
- Basic LED control
- WiFi connection
- Signal monitoring

### Week 3: Integration
- API consumer on Pico
- Access point mode
- Full system integration
- Testing

### Week 4: Documentation
- Write guides
- Create troubleshooting docs
- Build MkDocs site
- Final presentation

## Prerequisites

### Knowledge
- Basic Python programming
- HTML/CSS fundamentals
- Command line basics
- Text editor usage

### Hardware
- Computer (macOS, Windows, or Linux)
- Raspberry Pi Pico W
- Micro USB cable (data cable)
- WiFi network

### Software
- Python 3.12 or later
- Text editor or IDE
- Thonny IDE
- Web browser
- Git (optional but recommended)

## Success Criteria

You'll know you've successfully completed the project when:

- ✅ Web application runs and displays rotating numbers
- ✅ API responds to requests with correct data
- ✅ Pico W connects to WiFi successfully
- ✅ Pico W can consume API and display results
- ✅ Access point mode serves web interface
- ✅ All documentation is complete
- ✅ You can troubleshoot common issues
- ✅ Project is well-organized and documented

## Next Steps

Ready to begin? Follow these steps:

1. [Check Prerequisites](prerequisites.md) - Verify you have everything needed
2. [Quick Start Guide](quickstart.md) - Get up and running fast
3. [Install Thonny](../guides/thonny_installation.md) - Set up the Pico development environment
4. [Flash Your Pico](../guides/pico_flashing.md) - Prepare the hardware

## Questions?

- Check the [FAQ](../troubleshooting/faq.md)
- Review [Troubleshooting Guide](../troubleshooting/common_issues.md)
- Explore [Code Examples](../reference/examples.md)

---

Happy coding! 🚀
