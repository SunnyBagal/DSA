const websocket = require('ws');

const ws = new websocket('wss://stream.binance.com:9443/ws/btcusdt@trade');

ws.on('open', () => {
    console.log('Connected to Binance BTC stream');
});

ws.on('message', (data) => {
    const trade = JSON.parse(data);
    const price = Number(trade.p);
    const quantity = trade.q;
    const time = new Date(trade.T);

    console.log(`BTC Price: $${(price).toFixed(2)} | Quantity: ${quantity} | Time: ${time}`);
});

ws.on('close', () => {
    console.log('Connection closed');
});

ws.on('error', (error) => {
    console.error('Error:', error);
});
