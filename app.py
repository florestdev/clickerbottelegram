import flet # pip install flet

async def clicker(page: flet.Page) -> None:
    page.title = "Florest's Clicker"
    page.theme_mode = flet.ThemeMode.DARK # DARK / LIGHT / SYSTEM
    page.bgcolor = '#141221'
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.fonts = {"Sunday":"Sunday.ttf"}
    page.theme = flet.Theme(font_family='Sunday')
    user_agent = page.client_user_agent

    if "Mobile" in user_agent or "Android" in user_agent or "iPhone" in user_agent: 
        page.error("Устройство не поддерживается. Зайдите с ПК.")
        print(f'{page.client_ip} ({page.client_user_agent}): вход был отклонен.')
    elif "iPad" in user_agent or ("Macintosh" in user_agent and "Mobile" in user_agent): 
        page.error("Устройство не поддерживается. Зайдите с ПК.")
        print(f'{page.client_ip} ({page.client_user_agent}): вход был отклонен.')
    else:
            print(f'{page.client_ip} ({page.client_user_agent}): вход был одобрен.')
            async def score_up(event: flet.ContainerTapEvent) -> None:
                score.data += 1
                score.value = str(score.data)
                page.update()

            score = flet.Text("0", size=100, data=0)
            image = flet.Image('img.png', fit=flet.ImageFit.CONTAIN, animate_scale=flet.Animation(600, flet.AnimationCurve.EASE))
            page.add(score, flet.Container(flet.Stack([image]), on_click=score_up, margin=flet.Margin(0,0,0,30)))

if __name__ == '__main__':
    flet.app(target=clicker, view=None, port=50125)