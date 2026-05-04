const fs = require("fs");

// Try to parse string values as JSON
function tryParse(value) {
  if (typeof value === "string") {
    try {
      return JSON.parse(value); // removes \n, \", etc
    } catch (e) {
      return value;
    }
  }
  return value;
}

// Clean JSON structure
function cleanJsonString(data) {
  if (Array.isArray(data)) {
    return data.map(item => {
      const cleanedItem = {};
      for (const key in item) {
        cleanedItem[key] = tryParse(item[key]);
      }
      return cleanedItem;
    });
  } else if (typeof data === "object" && data !== null) {
    const cleanedObj = {};
    for (const key in data) {
      cleanedObj[key] = tryParse(data[key]);
    }
    return cleanedObj;
  } else {
    return data;
  }
}

// Read JSON file
function readJsonFile(filePath) {
  const raw = fs.readFileSync(filePath, "utf-8");
  return JSON.parse(raw);
}

// Main execution
const inputFile = "books/n8n-chatgpt-output.json";
const outputFile = "books/n8n-chatgpt-output-cleaned.json";

const data = readJsonFile(inputFile);
const cleanedData = cleanJsonString(data);

fs.writeFileSync(outputFile, JSON.stringify(cleanedData, null, 2), "utf-8");

console.log(`Cleaned data written to ${outputFile}`);