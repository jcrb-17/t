package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"strconv"
	"strings"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
	"github.com/go-chi/cors"
)

func main() {
	r := chi.NewRouter()
	r.Use(cors.Handler(cors.Options{
		AllowedOrigins:   []string{"https://*", "http://*"},
		AllowOriginFunc:  func(r *http.Request, origin string) bool { return true },
		AllowedMethods:   []string{"GET", "POST", "PUT", "DELETE", "OPTIONS"},
		AllowedHeaders:   []string{"Accept", "Authorization", "Content-Type", "X-CSRF-Token"},
		ExposedHeaders:   []string{"Link"},
		AllowCredentials: false,
		MaxAge:           300,
	}))
	r.Use(middleware.Logger)
	r.Get("/search/{value}/{pag}", func(w http.ResponseWriter, r *http.Request) {
		v1 := chi.URLParam(r, "value")
		v2, _ := strconv.Atoi(chi.URLParam(r, "pag"))
		json.NewEncoder(w).Encode(sendReq(v1, v2))
	})
	http.ListenAndServe(":3000", r)
	fmt.Println("listening on 3000")

}

func pr(val string) {
	fmt.Println("you entered " + val)
}

func sendReq(field string, pag int) string {
	q := `{
        "search_type": "matchphrase",
        "query":
        {
            "term": "%s"
        },
        "from": %d,
        "max_results": 20,
        "_source": []
    }`

	q = fmt.Sprintf(q, field, pag)

	req, err := http.NewRequest("POST", "http://localhost:4080/api/db/_search", strings.NewReader(q))
	if err != nil {
		log.Fatal(err)
	}
	req.SetBasicAuth(---user, ---pass)//zincsearch credentials
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()
	log.Println(resp.StatusCode)
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(body))
	return string(body)
}
