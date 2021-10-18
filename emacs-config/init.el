;; -------------------------------------------------------------------------------
;; Setup and package installation
;; -------------------------------------------------------------------------------

(setq
 +repo-dir (expand-file-name
            (concat (or load-file-name buffer-file-name) "/../.."))
 +note-dir (expand-file-name (format "%s/test-notes" +repo-dir))
 user-emacs-directory (expand-file-name
                       (format "%s/emacs-config/user-emacs-directory" +repo-dir))
 package-user-dir (expand-file-name (format "%s/emacs-config/elpa" +repo-dir)))

(package-initialize)
(setq package-archives '(("melpa-stable" . "https://stable.melpa.org/packages/")))
(unless package-archive-contents (package-refresh-contents))

(package-install-file (expand-file-name (format "%s/emacs-config/mvtn.tar" +repo-dir)))

(dolist (package '(rg ivy which-key))
  (unless (package-installed-p package)
    (package-install package)))

(require 'mvtn)
(require 'rg)

;; -------------------------------------------------------------------------------
;; Actual Configuration
;; -------------------------------------------------------------------------------

(ivy-mode 1)
(which-key-mode 1)

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
      mvtn-search-function 'mvtn-search-full-text-rg
      )

;; -------------------------------------------------------------------------------
;; Basic UI Tweaks
;; -------------------------------------------------------------------------------

(load-theme 'misterioso)
(menu-bar-mode 0)
(scroll-bar-mode 0)
(tool-bar-mode 0)