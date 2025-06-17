let agentCounter = document.querySelectorAll('input[name="agent[]"]').length;
let itemCounter = document.querySelectorAll('input[name="item[]"]').length;

function rebuildValuationTable() {
    const agents = Array.from(document.querySelectorAll('input[name="agent[]"]')).map(input => input.value || `Agent${Math.random().toString(36).substr(2, 3)}`);
    const items = Array.from(document.querySelectorAll('input[name="item[]"]')).map(input => input.value || `Item${Math.random().toString(36).substr(2, 3)}`);
    
    const tableBody = document.querySelector('table tbody');
    const tableHeadRow = document.querySelector('table thead tr');

    // Clear current table
    tableBody.innerHTML = '';
    tableHeadRow.innerHTML = '<th>Item \\ Agent</th>';
    
    agents.forEach(agent => {
        const th = document.createElement('th');
        th.textContent = agent;
        tableHeadRow.appendChild(th);
    });

    items.forEach(item => {
        const row = document.createElement('tr');
        const td = document.createElement('td');
        td.textContent = item;
        row.appendChild(td);
        agents.forEach(agent => {
            const cell = document.createElement('td');
            const input = document.createElement('input');
            input.type = 'number';
            input.min = '0';
            input.step = '0.1';
            input.name = `${agent}_${item}`;
            input.className = 'form-control';
            cell.appendChild(input);
            row.appendChild(cell);
        });
        tableBody.appendChild(row);
    });
}

document.getElementById('add-agent').addEventListener('click', function () {
    const container = document.getElementById('agents-container');
    const newAgent = document.createElement('div');
    newAgent.className = 'form-group';
    newAgent.innerHTML = `
        <input type="text" name="agent[]" placeholder="Agent name" required class="form-control">
    `;
    container.appendChild(newAgent);
    agentCounter++;
    rebuildValuationTable();
});

document.getElementById('add-item').addEventListener('click', function () {
    const container = document.getElementById('items-container');
    const newItem = document.createElement('div');
    newItem.className = 'form-group';
    newItem.innerHTML = `
        <input type="text" name="item[]" placeholder="Item name" required class="form-control">
    `;
    container.appendChild(newItem);
    itemCounter++;
    rebuildValuationTable();
});
