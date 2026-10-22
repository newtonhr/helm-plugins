# Helm tools this skill uses — and how they behave per access level

All tools live in the account-level connector **Marina_Ops - Helm**. It is not
bundled with this plugin. If the connector is missing, stop and say: "Ovaj razgovor
treba Helm — provjerite da je Marina_Ops - Helm uključen."

Helm knows who is asking. Each colleague has an access level; a tool refuses with
`requires one of [...]; got <level>` when the level is too low. **Treat a refusal as
a fact, record it, move on.** Never retry, never ask the colleague to change level.

Verified on 2026-09-18 with the `analyst` level. The live server decides what each
level may call; tool descriptions are only a hint.

## Tools this skill uses

| Tool | Use it for | analyst | Notes |
|---|---|---|---|
| `ping` | is Helm up | yes | first call if anything looks off |
| `health_check` | shop, database, logs, cache status | yes | baseline call in every request |
| `get_shop_config` | which shops exist, effective value of a setting | yes | `PS_SHOP_NAME` lists the shops; fix which shop the request is about |
| `get_configuration` / `list_configuration` | one or several shop settings | yes | prefer `get_shop_config` for the effective value |
| `search_products` | web-shop catalogue by name/code | yes | only what is published on the shop |
| `get_product` | one product: price, stock, categories | yes | by PrestaShop id from `search_products` |
| `pos_search_articles` | full warehouse/POS catalogue | yes | live stock, incoming, prices; matches name, internal code, Lalizas code; `total` quantifies scope with filters |
| `pos_get_article_by_code` / `pos_get_article_by_lalizas_code` | one article exactly | yes | prefer when the colleague gives an exact code |
| `pos_inventory_summary` | warehouse KPI snapshot and data-quality counters | yes | use when the wish touches stock, ordering, pricing |
| `pos_article_history`, `pos_price_changes`, `pos_top_movers`, `pos_dead_stock`, `pos_stockout_risk`, `pos_availability_events` | movement and history of articles | untested | only when the wish is about those topics |
| `pos_sync_status` | last POS ↔ shop sync runs | yes | when the wish is about POS or stock freshness |
| `list_orders` / `get_order` | recent orders, one order's lines | yes | `customer_email` may be present — never copy it into the request |
| `list_modules` / `get_module` | is a part of the shop installed, on which shops | yes | never propose building what is installed |
| `search_code` | does the shop already contain this feature | yes | **always with `subdir` = `modules` or `themes`**, `limit` 20; never without `subdir` |
| `search_logs` / `list_recent_errors` | error text the colleague quoted | yes | lane B only; source `prestashop` first, then `php-fpm` |

## Tools this skill does not use

| Tool | Why not |
|---|---|
| `read_file`, `list_dir`, `git_log`, `git_show`, `git_diff`, `git_blame` | The server's working files are not part of a request. Evidence comes from the catalogue, orders, modules and settings. |
| `agent_run`, `agent_status`, `agent_result`, `agent_list`, `agent_cancel`, `agent_continue` | Starts a longer server job that is not part of this conversation. |
| `fetch_storefront_url` | Does not return the page a customer sees in this version. |
| `get_customer_threads` | Customer personal data. |
| every `propose_*`, `review_plan`, `apply_plan`, `cancel_plan`, `list_plans`, `get_plan` | This skill never changes the shop. Lanes A and B hand off to a normal Helm task. |
| `create_db_backup`, `verify_backup_integrity`, `list_db_backups`, `list_source_backups`, `get_backup_status` | Operations, not request-writing. |
| `diagnose_performance`, `get_fpm_status`, `get_nginx_status`, `get_redis_info`, `get_disk_usage`, `get_service_status` | Operations; lane B hand-off may use them, this skill does not. |

## Delivery tools (may not exist yet)

| Tool | If present |
|---|---|
| `zahtjev_submit` | Send the finished Markdown with `vrsta`; report the returned id. |
| `zahtjev_status` / `zahtjev_list` | Tell the colleague they can ask for the status any time. |
| `zahtjev_answer` | Step 6: the colleague's answers to the analysis's questions P1, P2 …, all in one call, in their words — never your own. |
| `zahtjev_thread` | The whole thread of a request (messages and questions) when the colleague asks what was said. |
| `zahtjev_message` | A free message to Newton on an open request (an addition or correction after the answers). |

Detect by name at Step 5. If absent, fall back to a saved file — see SKILL.md.

## Degrade rules

1. Refusal (`requires one of ...`) → record "nije dostupno mojoj razini pristupa (<level>)" in the evidence table.
2. Empty result → record "nema podataka" — it is evidence too (a code missing from the web shop but present in the warehouse is a finding).
3. Timeout or connector error → try `ping` once; if it fails, finish the request with what you have and note "Helm nije bio dostupan za …".
4. About twelve tool calls per request. Priority: health → shops → modules → products/articles named → orders named → scope numbers → the rest.
