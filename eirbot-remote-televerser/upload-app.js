const express = require('express');
const { exec } = require('child_process');
const path = require('path');

const app = express();
const port = 3000;

app.use(express.static('public'));

app.post('/execute-script', (req, res) => {
  const pythonProcess = exec('python bin-sender.py', (error, stdout, stderr) => {
    if (error) {
      console.error('An error occurred while executing the Python script:', error);
      res.status(500).send('Error executing Python script');
    } else {
      console.log('Python script executed successfully!');
      res.status(200).send('Python script executed successfully');
    }
  });
});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'upload-app.html'));
});
  

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
