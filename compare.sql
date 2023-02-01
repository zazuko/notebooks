CREATE VIEW compare AS
SELECT "Int".obs AS obs,
"Int".total AS total_int,
"Apps".total AS total_apps,
"Int".total != "Apps".total AS is_total_different,
"Int".energie AS energie_int,
"Apps".energie AS energie_apps,
"Apps".energie != "Int".energie AS is_energie_different,
"Int".abgaben AS abgaben_int,
"Apps".abgaben AS abgaben_apps,
"Int".abgaben != "Apps".abgaben AS is_abgaben_different,
"Int".netznutzung AS netznutzung_int,
"Apps".netznutzung AS netznutzung_apps,
"Int".netznutzung != "Apps".netznutzung AS is_netznutzung_different,
"Int".foerderabgaben AS foerderabgaben_int,
"Apps".foerderabgaben AS foerderabgaben_apps,
"Apps".foerderabgaben != "Int".foerderabgaben AS is_foerderabgaben_different
FROM "Int"
FULL OUTER JOIN "Apps" ON "Int".obs = "Apps".obs
