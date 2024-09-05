import reflex as rx
from irrigation_proj.integration.forecast import integratedFunction

global weatherForecast 
weatherForecast = integratedFunction()

### TEST, COPY-PASTED FROM REFLEX SITE REMOVE AFTER LAYOUT ADJUSTMENTS
def line_features():
    return rx.recharts.line_chart(
        rx.recharts.line(
            data_key="humidity",
            type_="monotone",
            stroke="#e54d2e",
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
        rx.recharts.graphing_tooltip(),
        width="100%",
        height=300,
        data = [
            {"name": "7/24", "humidity": 68},
            {"name": "7/25","humidity": 64},
            {"name": "7/26","humidity": 67},
            {"name": "7/27","humidity": 53},
            {"name": "7/28","humidity": 52},
            {"name": "7/29","humidity": 58},
            {"name": "7/30","humidity": 40},
        ]
    )
###

# Individual forecast cards!
def forecastCard(day: str) -> rx.Component: 
    icon = ""
    if day == "Today":
        weatherData = weatherForecast[0]
    elif day == "Tomorrow":
        weatherData = weatherForecast[1]
    else:
        weatherData = weatherForecast[2]
    if "rain" in weatherData["weather"]:
        icon = "cloud-rain"
    elif "sun" in weatherData["weather"] or "sunny" in weatherData["weather"]:
        icon = "sun",
    elif "clouds" in weatherData["weather"] or "cloudy" in weatherData["weather"]:
        icon = "cloudy"
    return rx.card(
        rx.vstack(
            rx.icon(icon),
            rx.heading(day, size = "6"),
            rx.heading(weatherData["date"], size = "4"),
            rx.text(weatherData["weather"] + " is expected, with a forecasted temperature of " + str(weatherData["temp"]) + "°F"),
            align_content = "center",
            justify_content = "center",
            justify_items = "center",
            align_items = "center",
            justify = "center",
            align = "center",
        ),
        align_content = "center",
        justify_content = "center",
        justify_items = "center",
        align_items = "center",
        justify = "center",
        align = "center",
        width = "18vw",
    )

# Home page
def home():
    return rx.vstack(
        rx.flex(
            rx.image(
                src = "/logo.png",
                height = "8vh",
                width = "auto"
            ),
            width = "100vw",
            height = "10vh",
            background_color = "#00a2c7",
            align_items = "center"
        ),
        rx.scroll_area(
            rx.flex(
                rx.vstack(
                    rx.card(
                        rx.vstack(
                            rx.heading("Forecast and Past Weather", size = "7"),
                            rx.hstack(
                                rx.hstack(
                                    forecastCard("Today"),
                                    forecastCard("Tomorrow"),
                                    forecastCard("Day After Tomorrow"),
                                ),
                                rx.card(
                                    rx.vstack(
                                        rx.heading("Week's Weather Overview", size = "6"),
                                        line_features(),
                                        rx.chakra.button_group(
                                            rx.button("Humidity", color_scheme="tomato"),
                                            rx.button("Precipitation", color_scheme="grass"),
                                            rx.button("Temperature", color_scheme="cyan"),
                                            rx.button("Vapor Pressure Deficit", color_scheme="orange")
                                        )
                                    )
                                )
                            ),
                        ),
                        width = "95vw",
                    ),
                    rx.card(
                        rx.vstack(
                            rx.heading("Location Overview"),
                            rx.image(src="map1.png")
                        )
                    ),
                ),
                    align_content = "center",
                    justify_content = "center",
                    width = "100%"
            ),
            type="always",
            scrollbars="vertical",
        )
    )