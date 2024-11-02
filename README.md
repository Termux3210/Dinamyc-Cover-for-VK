# Cover Image Generator for VK

This project is a Python application that generates and uploads a custom cover image for a VKontakte (VK) user profile. The cover image features the current time and date over a randomly fetched background image.

### Features

- **Dynamic Background**: Fetches a random minimalistic wallpaper from an external source.
- **Customizable Text**: Displays the current time and date on the cover image.
- **Automatic Upload**: Automatically uploads the generated cover image to the user's VK profile.
- **Scheduled Updates**: Refreshes the cover image every 10 minutes.

### Requirements

To run this project, ensure you have the following installed:

- Python 3.7 or higher
- Required Python packages:
  - `aiohttp`
  - `Pillow`
  - `pendulum`
  - `python-dotenv`
  - `vkbottle`

You can install the required packages using pip:

```bash
pip install aiohttp Pillow pendulum python-dotenv vkbottle
```

### Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/vk-cover-image-generator.git
   cd vk-cover-image-generator
   ```

2. **Environment Variables**:

   Create a `.env` file in the root directory of your project and add your VK API token:

   ```plaintext
   TOKEN=your_vk_api_token
   ```

3. **User ID**:

   Update the `USER_ID` variable in `main.py` with your VK user ID.

### Usage

To run the application, execute the following command in your terminal:

```bash
python main.py
```

The application will start generating cover images and uploading them to your VK profile every 10 minutes.

### Code Overview

#### CoverImage Class

- **Attributes**:
  - `WIDTH`, `HEIGHT`: Dimensions of the cover image.
  - `FILL`, `STROKE_FILL`: Colors used for text.
  - `FONT`: Font file used for rendering text.

- **Methods**:
  - `_get_random_image()`: Fetches a random image from an external URL.
  - `draw_cover()`: Draws the current time and date on the fetched image.
  - `upload_cover()`: Uploads the generated cover image to VK.

#### Main Functionality

The main function initializes the API connection, creates an instance of `CoverImage`, and starts an infinite loop that generates and uploads a new cover image every 10 minutes.

### Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, please feel free to submit a pull request or open an issue.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Acknowledgments

- [VK API](https://vk.com/dev/manuals) for providing access to user profiles.
- [Pillow](https://python-pillow.org/) for image processing capabilities.
- [Pendulum](https://pendulum.eustace.io/) for easy date and time manipulation.

---

Feel free to modify this README as needed to better fit your project's specifics or any additional features you may add!
