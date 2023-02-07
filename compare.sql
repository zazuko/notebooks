CREATE VIEW compare AS
SELECT
"Int".obs AS obs,
"Int"."gemeindeName" AS gemeinde,
"Int".netzbetreiber AS netzbetreiber,
"Int".total AS total_int,
"Apps".total AS total_apps,
CASE
    WHEN "Apps".total = 0 THEN NULL
    ELSE ("Apps".total-"Int".total)/"Apps".total
END AS total_diff,
"Int".energie AS energie_int,
"Apps".energie AS energie_apps,
CASE
    WHEN "Apps".energie = 0 THEN NULL
    ELSE ("Apps".energie-"Int".energie)/"Apps".energie
END AS energie_diff,
"Int".abgaben AS abgaben_int,
"Apps".abgaben AS abgaben_apps,
CASE
    WHEN "Apps".abgaben = 0 THEN NULL
    ELSE ("Apps".abgaben-"Int".abgaben)/"Apps".abgaben
END AS abgaben_diff,
"Int".netznutzung AS netznutzung_int,
"Apps".netznutzung AS netznutzung_apps,
CASE
    WHEN "Apps".netznutzung = 0 THEN NULL
    ELSE ("Apps".netznutzung-"Int".netznutzung)/"Apps".netznutzung
END AS netznutzung_diff,
"Int".foerderabgaben AS foerderabgaben_int,
"Apps".foerderabgaben AS foerderabgaben_apps,
CASE
    WHEN "Apps".foerderabgaben = 0 THEN NULL
    ELSE ("Apps".foerderabgaben-"Int".foerderabgaben)/"Apps".foerderabgaben
END AS foerderabgaben_diff
FROM "Int"
FULL OUTER JOIN "Apps" ON "Int".obs = "Apps".obs
