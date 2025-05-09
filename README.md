# lagos-image-extraction
This project focuses on building a comprehensive image dataset of LEGO sets associated with specific Lagos IDs by scraping data from multiple LEGO-related websites. The primary goal is to extract high-quality set images and metadata from trusted sources and organize them for downstream use (e.g., ML training, cataloging, analysis).

Technologies Used:

    Python (requests, BeautifulSoup) for HTTP requests and HTML parsing.

    Pandas for structured data handling and export.

    dotenv for secure environment variable management (API keys, credentials if needed).

    Logging for request and error tracking.

    CSV/JSON for structured dataset output.

Websites Scraped:

    Brickset

    BrickLink

    Brick Economy

    Brick Owl

    ToyPro

Workflow Summary:

    Accept a list of Lagos IDs corresponding to LEGO sets.

    For each ID:

        Perform lookup across all five websites.

        Parse and extract set images, titles, and additional metadata.

        Save image URLs or download images to local storage/cloud.

    Final output is a structured dataset (CSV/JSON) containing all relevant image data per set.

Key Features:

    Handles multiple sources to ensure image redundancy and quality.

    Lightweight, non-Selenium approach for speed and efficiency.

    Modular design for easy extension or integration with other datasets or services.
