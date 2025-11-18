# XML Monitoring with Grafana and Prometheus

## Описание

Проект предназначен для мониторинга XML-данных (например, `cmd.pos.altitude`, `est.att.roll`) с веб-сервиса. 
Он включает в себя:

- **XML Exporter** — конвертирует значения из XML в метрики Prometheus.
- **Prometheus** — собирает метрики с Exporter'а.
- **Grafana** — отображает графики и алерты.

## Структура

```
xml-monitoring/
├── config.yaml            # Конфиг XML-параметров и их путей
├── exporter.py            # Flask-приложение, отдающее метрики
├── prometheus.yml         # Конфигурация Prometheus
├── docker-compose.yml     # Все сервисы: Grafana, Prometheus, Exporter
└── dashboards/            # (опц.) Grafana JSON dashboards
```

## Пример метрик

Пример XML:
```xml
<mandala>
  <cmd.pos.altitude>109.584</cmd.pos.altitude>
  <est.att.roll>0.477</est.att.roll>
</mandala>
```

Результат:
```
# HELP cmd_pos_altitude Altitude value
# TYPE cmd_pos_altitude gauge
cmd_pos_altitude 109.584
```

## Запуск

```bash
docker-compose up -d --build
```

Затем:

- **Grafana**: http://localhost:3000 (admin/admin)
- **Prometheus**: http://localhost:9191
- **Exporter**: http://localhost:9112/metrics

## Заметки

- Убедись, что источник XML доступен из контейнера (`host.docker.internal` или сетевой alias).
- Алерты можно настроить прямо в Grafana UI или через JSON.
