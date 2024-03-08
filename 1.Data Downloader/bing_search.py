import argparse
import asyncio
from playwright.async_api import async_playwright
import aiohttp
import os
from glob import glob
import re
from tqdm.auto import tqdm
try:
    main_data_path = glob('../data/')[0]
except:
    os.mkdir('../data/')
    main_data_path = glob('../data/')[0]
import json
p = re.compile('\d+')
with open('down.json') as f:
    before = json.load(f)

async def download_image(session, url, folder, index):
    response = await session.get(url)
    if response.status == 200:
        content = await response.read()
        file_path = os.path.join(main_data_path,folder, f'image_{index}.jpg')
        with open(file_path, 'wb') as file:
            file.write(content)

async def fetch_images(playwright, search_query, folder_name, num_images):
    # browser = await playwright.chromium.launch(headless=True)
    browser = await playwright.chromium.launch(headless=False)
    page = await browser.new_page()
    await page.goto(f'https://www.bing.com/images/search?q={search_query}')
    # 이미지를 저장할 폴더
    save_folder = folder_name
    os.makedirs(os.path.join(main_data_path,save_folder), exist_ok=True)
    max_image_i = glob(glob(os.path.join(main_data_path,save_folder))[0]+'/*.jpg')
    print(max_image_i)
    max_image_i.sort()
    try:
        max_image_i = int(p.findall(max_image_i[-1])[0])
    except Exception as e:
        print(e)
        max_image_i = 0

    async with aiohttp.ClientSession() as session:
        try:
            await page.click('a.iusc:first-child')
        except:
            await page.goto(f'https://www.bing.com/images/search?q={search_query}')
            await page.click('a.iusc:first-child')
        i=max_image_i
        index_i=0
        num_images += max_image_i
        with tqdm(total=num_images) as pbr:
            while num_images>index_i:
                try:
                    frame_locator = page.locator("iframe[id=OverlayIFrame]")
                    await frame_locator.wait_for(timeout=10000)

                    frame = await frame_locator.element_handle()
                    frame_content = await frame.content_frame()

                    await frame_content.wait_for_selector('img.nofocus', state="visible")
                    if index_i>max_image_i:
                        img_url = await frame_content.get_attribute('img.nofocus', 'src')
                        await download_image(session, img_url, save_folder, i)
                    await frame_content.click('div#navr')
                    index_i+=1
                    i+=1
                    pbr.update(1)
                except Exception as e:
                    index_i-=1
                    print(f'Error fetching image {i}:', str(e))
                    continue
    await browser.close()
async def main(search_query, folder_name):
    async with async_playwright() as playwright:
        await fetch_images(playwright, search_query, folder_name, 300)

procedures = {
    "Face Laser Toning before and after": ["얼굴 전체"],
    "Face Fractional Laser before and after": ["얼굴 전체"],
    "Face Vascular Laser before and after": ["빨간색 또는 보라색 혈관 부위"],
    "Face Genesis Laser before and after": ["얼굴 전체"],
    "Radiofrequency before and after": ["얼굴 전체", "몸 전체"],
    "Radiofrequency Microneedling before and after": ["얼굴 전체"],
    "High-Intensity Focused Ultrasound (HIFU) before and after": ["턱선", "볼 주변"],
    "Botox before and after in Jaw": ["턱"],
    "Botox before and after in Crow's Feet": ["눈가 주름 부위"],
    "Botox before and after in Forehead": ["이마"],
    "Botox before and after in Glabellar": ["눈썹 사이 주름 부위"],
    "Botox before and after in Perioral Lines": ["입 주변 주름 부위"],
    "Bunny Lines Botox before and after": ["코 주변 미소 주름"],
    "Botox before and after in Dimpled Chin": ["턱 아래 디플 효과"],
    "Face Filler before and after in Tear Troughs": ["눈 밑 눈밑 돌출"],
    "Face Filler before and after in Nasolabial Folds": ["코와 입 주위 굴곡 부위"],
    "Face Filler before and after in Lips": ["입술"],
    "Face Filler before and after in Temples": ["이마 측면"],
    "Face Filler before and after in Chin": ["턱"],
    "Face Filler before and after in Cheek": ["볼"],
    "Face Filler before and after in Nose": ["코"],
    "Face Filler before and after in Marionette Lines": ["입술 코너에서 아래로 향하는 주름"],
    "Face Thread Lifting before and after in Mid-Face Lift": ["중앙 부위", "볼"],
    "Face Thread Lifting before and after in Lower Face Lift": ["턱선", "아래 얼굴 부분"],
    "Face Thread Lifting before and after in Brow Lift": ["이마"],
    "Face Thread Lifting before and after in Neck Lift": ["목 부위"],
    "Face Thread Lifting before and after in Jowl Lift": ["턱 주변"],
    "Face Thread Lifting before and after in Eye Area Lift": ["눈 주변 부위"]
}
if __name__ == '__main__':
    # try:
    for i in procedures:
        folder = "_".join(i.split('before and after'))
        i = i+ ",".join(procedures[i])
        asyncio.run(main(i, folder))
