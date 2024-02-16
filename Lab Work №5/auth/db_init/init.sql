CREATE TABLE public."ApiSession" (
	session_id varchar NOT NULL,
	created_at date NOT NULL,
	CONSTRAINT "session_token_pkey" PRIMARY KEY (session_id)
);

CREATE INDEX "ix_ApiSession_session_id" ON public."ApiSession" USING btree (session_id);