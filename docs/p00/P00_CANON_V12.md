# P00 · Старт программы, инженерный метод и evidence discipline

- Статус: `MIGRATION_CANDIDATE`
- LAB status: `NOT_EXECUTED`
- PASS status: `NOT_ACHIEVED`
- Основной кейс: `P00-WEB-01`
- Граница выполнения: только собственная изолированная LAB

## 1. Назначение

P00 обучает полному инженерному циклу на компактном, но реальном Ubuntu/Nginx-контуре. Он не заменяет профильные P01–P20 и не выдаёт обзор роли за освоение профессии.

После P00 пользователь должен уметь:

- пройти целостный теоретический маршрут;
- развернуть минимальный сервис из Git;
- зафиксировать архитектуру и scope;
- применить защитную меру и телеметрию;
- выполнить контролируемый Run A;
- собрать и исследовать фактические артефакты;
- устранить root cause;
- провести сопоставимый Run B;
- выполнить backup, restore и regression;
- получить формальный Assurance decision;
- подготовить public-safe case study.

## 2. Архитектура кейса

```text
analyst01 · 10.10.10.10
        │
        │ isolated 10.10.10.0/24
        ▼
web01 · 10.10.10.20
Ubuntu Server + Nginx
        │
        ├── access/error logs
        ├── deployment and rollback scripts
        ├── bounded Bash detector
        └── private evidence vault
```

Никакие внешние цели, production-системы и чужие данные не входят в scope.

## 3. Сценарий

### Baseline

- Nginx отдаёт статическую страницу проекта.
- `/internal-check` существует как контролируемый canary path.
- Доступ к canary path в исходном состоянии ошибочно разрешён с analyst01.
- Access/error logs и service status доступны для сбора.
- Конфигурация, тесты и deployment scripts хранятся в Git.

### Run A

Attack выполняет заранее зафиксированную последовательность запросов к `/internal-check` и подтверждает доступ, который должен быть запрещён политикой.

Investigation связывает requests, status codes, timestamps, source host, Nginx logs, service state и configuration hash с общим `run_id`.

### Remediation

Defense и Application Security устраняют root cause в access policy. Delivery поставляет исправление через проверяемый deploy/rollback path. Detection получает детерминированные positive, negative и malformed fixtures.

### Run B

Используются те же основные цели, URL, request count, source profile и временное окно. Ожидаемый результат:

- доступ к canary path блокируется;
- normal path остаётся доступным;
- попытка фиксируется в telemetry;
- detector формирует ожидаемый результат;
- regression и recovery tests проходят.

## 4. Двухпроходная теория

### Проход 1

До основной практики полностью изучаются:

- основная литература P00;
- назначенные диапазоны по Git, Linux, HTTP, Nginx, evidence, threat modeling, incident handling, testing и recovery;
- обязательные статьи и видео;
- карта P00–P20 и R01–R26.

### Проход 2

Перед каждым LAB-блоком перечитываются точные разделы официальной документации и внешний источник практики.

## 5. Практические блоки

### L01. Repository и evidence baseline

- создать Git repository;
- определить private/public evidence boundary;
- создать evidence record template;
- выполнить clean-clone test;
- проверить отсутствие secrets.

### L02. LAB architecture и baseline

- проверить IP, routes, connectivity и service absence;
- зафиксировать snapshots;
- построить C4/DFD и trust boundary;
- отличить network failure от application failure.

### L03. Delivery baseline

- установить Nginx;
- создать конфигурацию в repository;
- реализовать deploy script с `nginx -t`, backup, reload и rollback;
- проверить normal request и baseline logs.

### L04. Control и Run A preparation

- создать canary path;
- формализовать expected status codes;
- подготовить Attack scenario, stop conditions и cleanup;
- заморозить Run A inputs.

### L05. Telemetry и detection

- определить обязательные log fields;
- реализовать bounded detector;
- добавить positive, negative, malformed и threshold fixtures;
- проверить exit codes, fail-closed/fail-open semantics и error handling.

### L06. Investigation и remediation

- собрать evidence manifest;
- нормализовать timestamps в UTC;
- построить timeline;
- разделить facts, assumptions и hypotheses;
- определить root cause;
- применить и проверить remediation.

### L07. Run B, recovery, assurance и portfolio

- выполнить сопоставимый Run B;
- проверить normal и blocked flows;
- восстановить конфигурацию из проверенного backup;
- выполнить regression;
- проверить evidence completeness;
- подготовить public-safe case study.

## 6. Минимальный вертикальный срез оркестрации

### ECP Scenario Controller

- загружает P00 scenario;
- создаёт `run_id`;
- проверяет scope;
- управляет workflow, checkpoints, resume и handoff.

### Delivery Orchestrator

- `plan`, `deploy`, `verify`, `rollback`;
- поставляет Nginx config, detector и service definitions;
- сохраняет deployment result и diff.

### Defense Orchestrator

- применяет access policy, service hardening и telemetry baseline;
- проверяет desired state и integrity;
- формирует defense result.

### Attack Orchestrator

- проверяет allowlist и stop conditions;
- выполняет frozen request sequence;
- сохраняет attacker-side timestamps и request results;
- выполняет cleanup.

### Investigation Orchestrator

- собирает logs и metadata;
- проверяет hashes;
- строит timeline;
- создаёт findings и incident report.

### Recovery Orchestrator

- создаёт backup/recovery point;
- проверяет integrity;
- выполняет restore/rollback;
- проверяет Nginx function после восстановления.

### Assurance Orchestrator

- выполняет functional, negative, malformed, regression и recovery tests;
- сравнивает Run A/Run B;
- проверяет evidence;
- выдаёт `PASS`, `FAIL`, `BLOCKED` или `NEEDS_REVIEW`.

## 7. Вклад R01–R26

| Роль | Реальная работа в P00 | Проверяемый результат |
|---|---|---|
| R01 GRC | Определить актив, риск, control objective и residual risk | `risk-register.md`, acceptance mapping |
| R02 Security Architecture | Зафиксировать C4/DFD, trust boundary и ADR | diagrams и ADR |
| R03 Network Security | Проверить адресацию, route, allowed/blocked flows | network baseline и test log |
| R04 Platform/Systems Security | Настроить Ubuntu/Nginx service baseline и hardening | config, service checks, diff |
| R05 Endpoint Security | Зафиксировать host/process/file integrity baseline | host baseline manifest |
| R06 Application Security | Проверить URI access logic и безопасную конфигурацию | access-control tests |
| R07 Cloud/Container Security | Проверить отсутствие внешних cloud dependencies/secrets и сформировать workload portability constraints | dependency/secrets check |
| R08 Identity Security | Определить service account, sudo boundary и least privilege | identity matrix и permission tests |
| R09 Data Security/Cryptography | Определить private/public data boundary и hash policy | evidence integrity policy и checksums |
| R10 Vulnerability Management | Зафиксировать versions, packages, known-risk review и remediation priority | version inventory и finding record |
| R11 Threat Modeling | Создать abuse case и threat/control mapping | threat model |
| R12 Threat Intelligence | Сопоставить сценарий с релевантными ATT&CK concepts и наблюдаемыми indicators | technique/indicator mapping |
| R13 Adversary Emulation | Выполнить Run A и Run B без выхода из LAB | attack manifests и cleanup evidence |
| R14 Detection Engineering | Реализовать и протестировать detector | rule/script, fixtures, test report |
| R15 SOC/Monitoring | Выполнить monitoring, triage и alert disposition | triage record |
| R16 Incident Response | Выполнить scope, containment, remediation и lessons learned | incident record |
| R17 DFIR | Сохранить evidence, построить timeline и подтвердить root cause | timeline и findings |
| R18 Threat Hunting | Проверить, есть ли аналогичные события вне известного marker | bounded hunt report |
| R19 Malware/Payload Analysis | Проанализировать request payload/headers и выделить воспроизводимые indicators без malware | payload analysis note |
| R20 QA/Security QA | Построить functional, negative, malformed и regression tests | test suite и report |
| R21 DevSecOps/Supply Chain | Реализовать delivery checks, provenance и clean-clone path | delivery manifest и SBOM/versions record where applicable |
| R22 Security Automation | Реализовать reusable scripts и structured outputs | automation package и tests |
| R23 Telemetry/Data Engineering | Определить event fields, UTC normalization и data-quality checks | telemetry schema и quality metrics |
| R24 Resilience/Recovery | Создать и проверить backup, restore, rollback, RTO/RPO | recovery report |
| R25 Documentation/Knowledge | Поддержать runbook, evidence index и technical explanation | documentation package |
| R26 Program/Portfolio Engineering | Проверить traceability и подготовить public-safe case study | release checklist и portfolio page |

## 8. PASS criteria

P00 получает PASS только если:

- теория первого прохода завершена и самопроверка пройдена;
- LAB развёртывается по документации;
- scope и safety checks проходят;
- Run A выполнен и подтверждён evidence;
- investigation подтверждает root cause;
- remediation поставлена через Delivery;
- Run B сопоставим и достигает ожидаемого результата;
- recovery фактически проверен;
- regression проходит;
- все применимые роли имеют реальные артефакты;
- public-safe package не содержит sensitive data;
- Assurance выдаёт PASS.

## 9. Сохранение старого P00

Сценарий configuration/symlink tampering из старых P00 не удаляется и не смешивается с вводным кейсом. Он получает статус `P00-EXT-01 · DEEP_EXTENSION` до отдельного решения о переносе в P05, P12 или P18.
