(import bakery [ls])
(import oreo)
(import oreo [nots?])
(import pathlib [Path])
(require hyrule [->])
(setv cookies (/ (.resolve (. (Path __file__) parent parent) :strict True) "cookies"))
(setv cookies-ls (.ls oreo cookies))
(setv assorted-cookies (.ls oreo cookies :sort True))
(import oreo [hidden?])
(defn test-bakery [] (-> assorted-cookies (= (ls :m/list True cookies :m/sort None :m/filter #(True hidden?))) (assert)))
(defn test-program-options [] (-> assorted-cookies (= (ls :m/list True :a True cookies :m/sort None :m/filter nots?)) (assert)))
