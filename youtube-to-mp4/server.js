const express = require('express');
const { exec } = require('child_process');
const path = require('path');

const app = express();
const port = 3000;

app.use(express.static('public'));
app.use(express.json());

app.post('/download', (req, res) => {
    const { url } = req.body;
    if (!url) {
        return res.status(400).send('URL is required');
    }

    const outputPath = path.join(__dirname, 'downloads', '%(title)s.%(ext)s');
    const command = `yt-dlp -f 'best[ext=mp4]' -o '${outputPath}' ${url}`;

    exec(command, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error: ${stderr}`);
            return res.status(500).send(`Error downloading video: ${stderr}`);
        }
        console.log(`Output: ${stdout}`);
        res.send('Download started successfully');
    });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
