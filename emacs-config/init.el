(load-theme 'tango-dark)

(require 'mvtn)

(setq
 +repo-dir (expand-file-name
            (concat (or load-file-name buffer-file-name) "/../.."))
 +note-dir (expand-file-name (format "%s/test-notes" +repo-dir))
 package-user-dir (expand-file-name (format "%s/emacs-config/elpa"
                                                 +repo-dir)))

(package-install-file (expand-file-name (format "%s/emacs-config/mvtn.tar" +repo-dir)))

(setq mvtn-note-directories
      (list (list :dir (concat +note-dir "/prv") :name "prv" :structure
                  '((:dir "flt" :datetree t)
                    (:dir "ztk" :datetree t)
                    (:dir "tec" :datetree t)
                    (:dir "stc" :datetree nil)))
            (list :dir (concat +note-dir "/wrk") :name "wrk" :structure
                  '((:dir "flt" :datetree t)
                    (:dir "stc" :datetree nil))))
      mvtn-default-file-extension "org"
      ;; mvtn-search-function 'mvtn-search-full-text-rg
      )